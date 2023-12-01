import cv2

src = cv2.imread("F:\dev\opencv\image\S1000rr.jpg")

dst = src.copy()


roi = src[100:600, 200:700]
dst[0:500, 0:500] = roi

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()