import cv2
import numpy as np
import argparse

src1 = cv2.imread('./image/scr_home_0.bmp', cv2.IMREAD_COLOR)
crop = src1.copy()
crop = src1[0:300, 75:725]


cv2.imshow('origin', src1)
cv2.imshow('crop', crop)

cv2.waitKey()
cv2.destroyAllWindows()