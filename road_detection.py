import cv2
import numpy as np

# Load image
img = cv2.imread("static/campus_map.png")

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Detect dark gray roads
lower = np.array([0, 0, 120])
upper = np.array([179, 40, 245])

road_mask = cv2.inRange(hsv, lower, upper)

# Remove noise
kernel = np.ones((3,3), np.uint8)

road_mask = cv2.morphologyEx(
    road_mask,
    cv2.MORPH_OPEN,
    kernel
)

cv2.imshow("Road Mask", road_mask)

cv2.imwrite(
    "static/road_mask.png",
    road_mask
)

cv2.waitKey(0)
cv2.destroyAllWindows()
