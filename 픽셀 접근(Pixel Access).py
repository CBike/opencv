import cv2
import numpy as np


gray = np.linspace(0, 255, num=90000, endpoint=True, retstep=False, dtype=np.uint8).reshape(300, 300, 1)
color = np.zeros((300, 300, 3), np.uint8)
color[0:150, :, 0] = gray[0:150, :, 0]
color[:, 150:300, 2] = gray[:, 150:300, 0]

x, y, c = 200, 100, 0

access_gray = gray[y, x, c]
access_color_blue = gray[:, 150:300, 0]
access_color = color[y, x]

print(access_gray)
print(access_color_blue)
print(access_color)

cv2.imshow("gray", gray)
cv2.imshow("color", color)
cv2.waitKey(0)
cv2.destroyAllWindows()