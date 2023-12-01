import cv2

src = cv2.imread("F:\dev\opencv\image\S1000rr.jpg", cv2.IMREAD_COLOR)

dst = src[100:600, 200:700].copy()

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()