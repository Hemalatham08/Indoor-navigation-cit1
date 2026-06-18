import csv
import math
from wifi_scan import scan_wifi

# Get current WiFi signals automatically
current_signal = scan_wifi()

print("Current WiFi Signals:")
print(current_signal)

best_location = None
smallest_distance = float('inf')

# Open fingerprint dataset
with open("wifi_fingerprint.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        # Get values safely
        hema = current_signal.get("Hema", 0)
        island = current_signal.get("island-0B6BF0", 0)
        d2s = current_signal.get("D2S COMPUTERS", 0)

        # Calculate Euclidean distance
        distance = math.sqrt(
            (int(row["Hema"]) - hema) ** 2 +
            (int(row["island"]) - island) ** 2 +
            (int(row["D2S"]) - d2s) ** 2
        )

        print(f"{row['Location']} --> Distance = {distance}")

        # Find closest location
        if distance < smallest_distance:
            smallest_distance = distance
            best_location = row["Location"]

# Final prediction
print("\nPredicted Location:", best_location)
with open("current_location.txt", "w") as file:
    file.write(best_location)

print("Location written to current_location.txt")