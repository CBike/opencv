import numpy as np
import cv2

src = cv2.imread("./image/highway.JPG")
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
canny = cv2.Canny(gray, 400, 100, apertureSize=3, L2gradient=True)
# lines = cv2.HoughLines(canny, 0.8, np.pi / 180, 150, srn=100, stn=200, min_theta=0, max_theta=np.pi)
#
# for i in lines:
#     rho, theta = i[0][0], i[0][1]
#     a, b = np.cos(theta), np.sin(theta)
#     x0, y0 = a*rho, b*rho
#     scale = src.shape[0] + src.shape[1]
#
#     x1 = int(x0 + scale * -b)
#     y1 = int(y0 + scale * a)
#     x2 = int(x0 - scale * -b)
#     y2 = int(y0 - scale * a)
#
#     cv2.line(dst, (x1, y1), (x2, y2), (0, 0, 255), 2)
#     cv2.circle(dst, (int(x0), int(y0)), 3, (255, 0, 0), 5, cv2.FILLED)

lines = cv2.HoughLinesP(canny, 0.8, np.pi / 180, 90, minLineLength=10, maxLineGap=100)

for i in lines:
    cv2.line(dst, (int(i[0][0]), int(i[0][1])), (int(i[0][2]), int(i[0][3])), (0, 0, 255), 2)


cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()