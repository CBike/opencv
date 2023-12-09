import cv2

src = cv2.imread("./image/beach.JPG")
dst = cv2.applyColorMap(src, cv2.COLORMAP_OCEAN)

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()