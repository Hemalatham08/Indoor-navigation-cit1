rssi = -53   # Example value

if rssi >= -40:
    progress = 100

elif rssi >= -58:
    progress = 75

elif rssi >= -77:
    progress = 50

else:
    progress = 0

with open("progress.txt", "w") as file:
    file.write(str(progress))

print("Progress =", progress)