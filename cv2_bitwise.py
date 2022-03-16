import cv2
import numpy as np

src1 = cv2.imread('./image/S1000rr.jpg',cv2.IMREAD_COLOR)
src2 = cv2.imread('./image/S1000rr_grayscale.jpg',cv2.IMREAD_COLOR)


bitAnd = cv2.bitwise_and(src1, src2)
bitOr = cv2.bitwise_or(src1, src2)
bitXor = cv2.bitwise_xor(src1, src2)
cv2.imshow('origi', src1)
cv2.imshow('bitAnd',bitAnd)
cv2.imshow('bitOr',bitOr)
cv2.imshow('bitXor',bitXor)

cv2.waitKey()
cv2.destroyAllWindows()