import cv2


def onChange(pos):

    pass

src = cv2.imread('./image/cherryblossom.JPG', cv2.IMREAD_GRAYSCALE)

cv2.namedWindow("Trackbar Windows")
cv2.createTrackbar("Threshold", "Trackbar Windows", 0, 255, onChange)
cv2.createTrackbar("maxValue", "Trackbar Windows", 0, 255, lambda x: x)
cv2.setTrackbarPos("Threshold", "Trackbar Windows", 127)
cv2.setTrackbarPos("maxValue", "Trackbar Windows", 255)

while cv2.waitKey(1) != ord('q'):

    thresh = cv2.getTrackbarPos("Threshold", "Trackbar Windows")
    maxval = cv2.getTrackbarPos("maxValue", "Trackbar Windows")

    _, binary = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)

    cv2.imshow("Trackbar Windows", binary)



cv2.destroyAllWindows()