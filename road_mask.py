import cv2
import numpy as np
# Load image
img = cv2.imread("static/campus_map.png")

# Resize optional
# img = cv2.resize(img, (1200, 800))

# Convert to grayscale
gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

# Threshold
_, thresh = cv2.threshold(
    gray,
    120,
    255,
    cv2.THRESH_BINARY_INV
)

# CONNECT BROKEN ROADS
kernel = np.ones((5,5), np.uint8)

thresh = cv2.morphologyEx(
    thresh,
    cv2.MORPH_CLOSE,
    kernel
)

# Show output
cv2.imshow("Road Mask", thresh)

# Save image
cv2.imwrite(
    "static/road_mask.png",
    thresh
)

cv2.waitKey(0)
cv2.destroyAllWindows()