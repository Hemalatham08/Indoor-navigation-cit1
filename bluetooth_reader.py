import serial

for port in ["COM4", "COM5","COM6"]:
    try:
        print("Testing", port)

        ser = serial.Serial(port, 9600, timeout=3)

        data = ser.readline()

        print("Received:", data)

        ser.close()

    except Exception as e:
        print(port, e)