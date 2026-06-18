from collections import deque
import cv2

def find_path(start, end, mask_path):

    img = cv2.imread(mask_path, 0)

    queue = deque([[start]])
    visited = set()

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:

        path = queue.popleft()
        x, y = path[-1]

        if (x, y) == end:
            return path

        if (x, y) not in visited:

            visited.add((x, y))

            for dx, dy in directions:

                nx, ny = x+dx, y+dy

                if 0 <= nx < img.shape[1] and 0 <= ny < img.shape[0]:

                    if img[ny, nx] > 200:

                        queue.append(path + [(nx, ny)])
                        
    print("Total points",len(path))
    print("Start Pixel:", img[start[1], start[0]])
    print("End Pixel:", img[end[1], end[0]])    
    return None

def draw_path(path):

    img = cv2.imread("static/campus_map.png")

    for point in path:
        cv2.circle(img, point, 2, (0,0,255), -1)

    # for i in range(len(path)-1):

        #cv2.line(
            #img,
           # path[i],
          #  path[i+1],
          #  (0,0,255),
         #   5
        #)
    cv2.imwrite("static/output.png", img)
    print("output.png saved")