import cv2


src = cv2.imread("F:\dev\opencv\image\S1000rr.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

ret, dst = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()

