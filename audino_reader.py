import serial

ser = serial.Serial("COM6",9600)

while True:
    location = ser.readline().decode(errors="ignore").strip()

    if location:
        print("Received:", location)

        with open("current_location.txt","w") as f:
            f.write(location)
              