import cv2
import numpy as np
from collections import deque

# LOAD ROAD MASK
img = cv2.imread(
    "static/road_mask.png",
    0
)
color_map = cv2.imread(
    "static/campus_map.png"
)

# CHECK IMAGE
if img is None:
    print("Image not loaded")
    exit()

# SOURCE POINT
start = (1108, 750)

# DESTINATION POINT
end = (775,572)

print("Start Pixel Value:",
      img[start[1], start[0]])

print("End Pixel Value:",
      img[end[1], end[0]])
# CREATE VISITED SET
visited = set()

# BFS QUEUE
queue = deque([[start]])

# 4 DIRECTIONS
directions = [
    (0,1),
    (1,0),
    (0,-1),
    (-1,0)
]

# FINAL PATH
found_path = None

# BFS LOOP
while queue:

    path = queue.popleft()

    x, y = path[-1]

    # DESTINATION FOUND
    if (x, y) == end:

        found_path = path
        break

    # VISIT NODE
    if (x, y) not in visited:

        visited.add((x, y))

        # CHECK ALL DIRECTIONS
        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            # IMAGE BOUNDARY CHECK
            if (
                0 <= nx < img.shape[1]
                and
                0 <= ny < img.shape[0]
            ):

                # MOVE ONLY ON WHITE ROAD
                if img[ny, nx] > 200:

                    new_path = list(path)
                    new_path.append((nx, ny))

                    queue.append(new_path)

# DRAW PATH
if found_path:

    for point in found_path:

        cv2.circle(
            color_map,
            point,
            1,
            (0,0,255),
            -1
        )

# DRAW SOURCE
cv2.circle(
    color_map,
    start,
    8,
    (0,255,0),
    -1
)

# DRAW DESTINATION
cv2.circle(
    color_map,
    end,
    8,
    (255,0,0),
    -1
)

# SHOW RESULT
cv2.imshow(
    "Road Navigation",
    color_map
)
cv2.waitKey(0)
cv2.destroyAllWindows()