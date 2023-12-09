import cv2
import numpy as np

src = cv2.imread("./image/newyork.JPG")
height, width = src.shape[:2]
map2, map1, = np.indices((height, width), dtype=np.float32)

map1 = map1 + width / 100 * np.sin(map1)
map2 = map2 + height / 100 * np.cos(map2)

dst = cv2.remap(src, map1, map2, cv2.INTER_CUBIC)

cv2.imshow("dst", dst)
cv2.waitKey()