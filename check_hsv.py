import cv2

# Load image
img = cv2.imread("static/campus_map.png")

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Function to print HSV value when clicked
def get_hsv(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        print("Pixel Position:", x, y)
        print("HSV Value:", hsv[y, x])
        print("-------------------")

# Create window
cv2.namedWindow("Campus Map")

# Attach mouse click event
cv2.setMouseCallback("Campus Map", get_hsv)

# Keep window open
while True:

    cv2.imshow("Campus Map", img)

    if cv2.waitKey(1) & 0xFF == 27:   # ESC key
        break

cv2.destroyAllWindows()