import webbrowser
import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Create QR detector
detector = cv2.QRCodeDetector()

while True:

    success, frame = cap.read()

    # Detect and decode QR
    data, bbox, _ = detector.detectAndDecode(frame)

    # If QR detected
    if data:

        print("Detected:", data)

       # with open("current_location.txt", "w") as file:

         #   file.write(data)

        # Save current location
        #with open("current_location.txt", "w") as file:

         #   file.write(data)
        webbrowser.open(data)
        break
        # Draw QR boundary
        if bbox is not None:

            points = bbox.astype(int)

            for i in range(len(points[0])):

                pt1 = tuple(points[0][i])

                pt2 = tuple(
                    points[0][(i + 1) % len(points[0])]
                )

                cv2.line(
                    frame,
                    pt1,
                    pt2,
                    (0,255,0),
                    3
                )

        # Show text
        cv2.putText(
            frame,
            data,
            (50,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            2
        )

    # Show webcam
    cv2.imshow("QR Scanner", frame)

    # ESC to exit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()