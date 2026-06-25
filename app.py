import shutil

rssi_data = {
    "Gate1": -100,
    "MainBlock": -100,
    "Auditorium": -100
}
gps_data = {
    "lat": 0,
    "lon": 0
}
def reset_map():
    try:
        shutil.copy(
            "static/campus_map.png",
            "static/output.png"
        )
        print("Map reset")
    except Exception as e:
        print("Reset error:", e)

def update_current_location():
    location = max(
        rssi_data,
        key=rssi_data.get
    )

    try:
        with open("current_location.txt", "r") as f:
            previous = f.read().strip()
    except:
        previous = ""

    if location != previous:
        print(f"Location changed: {previous} → {location}")
        reset_map()

    with open("current_location.txt", "w") as file:
        file.write(location)

    print("Current Location:", location)

def calculate_progress(source, destination):
    try:
        with open("original_source.txt", "r") as f:
            original_source = f.read().strip()
    except:
        return 0

    if not original_source:
        return 0

    if source == destination:
        return 100

    if original_source not in nodes or destination not in nodes or source not in nodes:
        return 0

    # Total path from original source to destination
    total_path = find_path(
        nodes[original_source],
        nodes[destination],
        "static/road_mask.png"
    )

    # Remaining path from current source to destination
    remaining_path = find_path(
        nodes[source],
        nodes[destination],
        "static/road_mask.png"
    )

    if not total_path or not remaining_path:
        return 0

    total_len = len(total_path)
    remaining_len = len(remaining_path)
    completed_len = total_len - remaining_len

    if total_len == 0:
        return 0

    progress = int((completed_len / total_len) * 100)
    print(f"Progress: {progress}% | {original_source} → {source} → {destination}")
    return progress

from flask import Flask, render_template, request, jsonify
import cv2
import time
from path_engine import draw_path
from path_engine import find_path
from graph import nodes

app = Flask(__name__)

@app.route("/current_location")
def current_location():
    try:
        with open("current_location.txt", "r") as f:
            location = f.read().strip()
    except:
        location = "Unknown"
    return location

@app.route("/update_rssi", methods=["POST"])
def update_rssi():
    print("================================")
    print("UPDATE_RSSI ENDPOINT HIT")
    data = request.json
    print("RAW DATA:", data)
    node = data["node"]
    rssi = data["rssi"]
    print("NODE:", node)
    print("RSSI:", rssi)
    rssi_data[node] = rssi
    update_current_location()
    print("RSSI TABLE:", rssi_data)
    print("================================")
    return jsonify({"status": "ok"})

# Welcome page
@app.route("/")
def welcome():
     # If QR code included a source parameter, use it
    qr_source = request.args.get("source")
    if qr_source:
        with open("current_location.txt", "w") as f:
            f.write(qr_source)
        print("Source set from QR scan:", qr_source)

    try:
        with open("current_location.txt", "r") as file:
            source = file.read().strip()
    except:
        source = ""

    # Save original source only once
    if source:
        try:
            with open("original_source.txt", "r") as f:
                existing = f.read().strip()
        except:
            existing = ""

        if not existing:
            with open("original_source.txt", "w") as f:
                f.write(source)
            print("Original source saved:", source)

    return render_template("welcome.html", source=source)

# Map preview page
@app.route("/map")
def map_page():
    try:
        with open("current_location.txt", "r") as file:
            source = file.read().strip()
    except:
        source = ""

    marker_x = 0
    marker_y = 0

    if source in nodes:
        marker_x, marker_y = nodes[source]

    return render_template(
        "map_preview.html",
        source=source,
        marker_x=marker_x,
        marker_y=marker_y
    )

# Navigation page
@app.route("/navigation", methods=["GET", "POST"])
def navigation():
    # Always read live location
    try:
        with open("current_location.txt", "r") as file:
            source = file.read().strip()
    except:
        source = ""

    print("Live source:", source)

    marker_x = 0
    marker_y = 0
    if source in nodes:
        marker_x, marker_y = nodes[source]

    destination = ""
    path = []

    if request.method == "POST":
        destination = request.form["destination"]
        print("Destination selected:", destination)

        # Save destination
        with open("destination.txt", "w") as f:
            f.write(destination)

        # Save original source when journey starts
        with open("original_source.txt", "w") as f:
            f.write(source)
        print("Journey started from:", source)

    else:
        # Load saved destination on refresh
        try:
            with open("destination.txt", "r") as f:
                destination = f.read().strip()
        except:
            destination = ""

    # Calculate and draw path
    if source in nodes and destination in nodes:
        start = nodes[source]
        end = nodes[destination]

        path = find_path(
            start,
            end,
            "static/road_mask.png"
        )

        if path:
            # Calculate progress
            progress = calculate_progress(source, destination)

            # Remove completed portion of path
            points_to_remove = int(len(path) * progress / 100)
            remaining_path = path[points_to_remove:]

            if remaining_path:
                draw_path(remaining_path)
                print(f"Path drawn: {source} → {destination} | {progress}% completed")
            else:
                # Journey complete
                reset_map()
                print("Journey complete! Arrived at", destination)
        else:
            print("No path found")
    else:
        reset_map()

    # Check if arrived
    arrived = (source == destination and destination != "")

    return render_template(
        "index.html",
        source=source,
        destination=destination,
        nodes=nodes,
        path=path,
        marker_x=marker_x,
        marker_y=marker_y,
        arrived=arrived,
        time=int(time.time())
    )

# Progress update
@app.route("/update_progress/<int:value>")
def update_progress(value):
    with open("progress.txt", "w") as file:
        file.write(str(value))
    return f"Progress Updated: {value}"

# Reset journey
@app.route("/reset")
def reset_journey():
    try:
        with open("original_source.txt", "w") as f:
            f.write("")
        with open("destination.txt", "w") as f:
            f.write("")
        reset_map()
        print("Journey reset")
    except:
        pass
    return jsonify({"status": "reset ok"})
@app.route("/debug")
def debug():
    try:
        with open("current_location.txt") as f:
            current = f.read().strip()
    except:
        current = "missing"

    try:
        with open("destination.txt") as f:
            dest = f.read().strip()
    except:
        dest = "missing"

    try:
        with open("original_source.txt") as f:
            original = f.read().strip()
    except:
        original = "missing"

    progress = 0
    if current in nodes and dest in nodes:
        progress = calculate_progress(current, dest)

    return jsonify({
        "current_location": current,
        "destination": dest,
        "original_source": original,
        "progress": progress
    })
@app.route("/update_gps", methods=["POST"])
def update_gps():

    data = request.json

    gps_data["lat"] = data["lat"]
    gps_data["lon"] = data["lon"]

    print(
        "GPS Received:",
        gps_data["lat"],
        gps_data["lon"]
    )

    return jsonify({
        "status": "ok"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )