import cv2
import numpy as np

src = cv2.imread("./image/nightroad.JPG")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
result = np.zeros((src.shape[0], 256), dtype=np.uint8)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
cv2.normalize(hist, hist, 0, result.shape[0], cv2.NORM_MINMAX)


for x, y in enumerate(hist):
    cv2.line(result, (int(x), result.shape[0]), (int(x), result.shape[0] - int(y)), 255)

dst = np.hstack([gray, result])


cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()