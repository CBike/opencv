import numpy as np
import cv2

img1 = cv2.imread('./image/S1000rr.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('./image/S1000rr.jpg.jpg',cv2.IMREAD_COLOR)

diff = cv2.absdiff(img1,img2)

cv2.imshow('diff',diff)
cv2.waitKey()
cv2.destroyAllWindows()