import numpy as np
import cv2


src = cv2.imread("./image/zebra.JPG")


kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))
dilate = cv2.dilate(src, kernel, anchor=(-1, -1), iterations=5)
erode = cv2.erode(src, kernel, anchor=(-1, -1), iterations=5)

dst = np.concatenate((src, dilate, erode), axis=0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()