import numpy as np
import cv2

src = cv2.imread("./image/flower.JPG")

data = src.reshape(-1, 3).astype(np.float32)
criteria = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 10, 0.001)
retval, bastLabels, centers = cv2.kmeans(data, 5, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

centers = centers.astype(np.uint8)
dst = centers[bastLabels].reshape(src.shape)


cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()

