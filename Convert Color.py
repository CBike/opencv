import cv2
src = cv2.imread("F:\dev\opencv\image\S1000rr.jpg", cv2.IMREAD_COLOR)

dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

cv2.imshow("src", src)
cv2.imshow("dst", dst)


cv2.waitKey()
cv2.destroyAllWindows()