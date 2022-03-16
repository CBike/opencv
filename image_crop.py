import cv2
import numpy as np
import argparse

src1 = cv2.imread('./image/S1000rr.jpg', cv2.IMREAD_COLOR)
crop = src1.copy()
crop = src1[0:450, 60:740]
cv2.imshow('origin', src1)
cv2.imshow('crop', crop)

cv2.waitKey()
cv2.destroyAllWindows()