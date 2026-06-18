import serial
import requests
import time
import threading

FLASK_URL = "http://127.0.0.1:5000/update_rssi"

# Add all 3 COM ports here
PORTS = [
    "COM7",  # Gate1 ESP32
    "COM3",  # MainBlock ESP32  
    #"COM5",  # Auditorium ESP32
]

def read_port(port):
    try:
        ser = serial.Serial(port, 115200, timeout=1)
        time.sleep(2)
        print(f"Reading from {port}")
        while True:
            try:
                line = ser.readline().decode("utf-8").strip()
                if line.startswith("RSSI:"):
                    parts = line.split(":")
                    node = parts[1]
                    rssi = int(parts[2])
                    print(f"[{port}] {node} = {rssi}")
                    try:
                        response = requests.post(FLASK_URL, json={
                            "node": node,
                            "rssi": rssi
                        })
                        print(f"Flask: {response.json()}")
                    except Exception as e:
                        print(f"Flask error: {e}")
            except Exception as e:
                print(f"Read error on {port}: {e}")
                time.sleep(1)
    except Exception as e:
        print(f"Cannot open {port}: {e}")

# Start one thread per ESP32
for port in PORTS:
    t = threading.Thread(target=read_port, args=(port,))
    t.daemon = True
    t.start()

# Keep main thread alive
while True:
    time.sleep(1)