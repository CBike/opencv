import cv2

src = cv2.imread("./image/hats.JPG", cv2.IMREAD_GRAYSCALE)
templit = cv2.imread("./image/hat.JPG", cv2.IMREAD_GRAYSCALE)
dst = cv2.imread("./image/hats.JPG")


result = cv2.matchTemplate(src, templit, cv2.TM_SQDIFF_NORMED)

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
x, y = minLoc
h, w = templit.shape

dst = cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 0, 255), 1)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()