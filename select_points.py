import cv2

# Load image
img = cv2.imread("static/campus_map.png")

# Check image loaded
if img is None:
    print("Image not loaded")
    exit()

# Store points
points = []
def mouse_click(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:

        print("Clicked:", x, y)

        points.append((x, y))

        # FIRST POINT
        if len(points) == 1:

            cv2.circle(
                img,
                (x, y),
                8,
                (0,255,0),
                -1
            )

        # SECOND POINT
        elif len(points) == 2:

            cv2.circle(
                img,
                (x, y),
                8,
                (0,0,255),
                -1
            )

            # DRAW RED LINE
            cv2.line(
                img,
                points[0],
                points[1],
                (0,0,255),
                5
            )

        # REFRESH WINDOW
        cv2.imshow("Select Points", img)

# Create window
cv2.namedWindow("Select Points")

# Show image
cv2.imshow("Select Points", img)

# Connect mouse function
cv2.setMouseCallback(
    "Select Points",
    mouse_click
)

# Keep window open
cv2.waitKey(0)

cv2.destroyAllWindows()

print("Selected Points:", points)