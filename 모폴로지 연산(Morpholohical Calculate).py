import numpy as np
import cv2


src = cv2.imread('./image/mopology.JPG')


kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))
dst = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel, iterations=9)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()