import cv2

src = cv2.imread("image/S1000rr.jpg")
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)

cv2.imshow("h", h)
cv2.imshow("s", s)
cv2.imshow("v", v)

cv2.waitKey()
cv2.destroyAllWindows()