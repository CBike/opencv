import cv2
import numpy as np
import argparse

src1 = cv2.imread('./image/S1000rr.jpg.bmp', cv2.IMREAD_COLOR)
cv2.imshow('before',src1)
result = cv2.rectangle(src1,(740,15),(800,40),(0,0,0),-1)



cv2.imshow('after',src1)
cv2.waitKey()
cv2.destroyAllWindows()