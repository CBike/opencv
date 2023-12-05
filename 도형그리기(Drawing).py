import cv2
import numpy as np

src = np.zeros((763, 1366, 3), dtype=np.uint8)
src = cv2.line(src, (100, 100), (1200, 100), (0, 0, 255), 3, cv2.LINE_AA)
src = cv2.circle(src, (300, 300), 50, (0, 255, 0), cv2.FILLED, cv2.LINE_4)
src = cv2.rectangle(src, (500,200), (1000, 400), (255, 0, 0), 5, cv2.LINE_8)
src = cv2.ellipse(src, (1200, 300), (100, 50), 0, 90, 180, (255, 255, 0), 2)

pts1 = np.array([[100, 500], [300, 500], [200, 600]])
pts2 = np.array([[600, 500], [800, 500], [700, 600]])
src = cv2.polylines(src, [pts1], True, (0, 255, 255), 2)
src = cv2.fillPoly(src, [pts2], (255, 0, 255), cv2.LINE_AA)

src = cv2.putText(src, "CBIKE", (900, 600), cv2.FONT_HERSHEY_COMPLEX, 2,(255, 255, 255), 3)

cv2.imshow("src", src)
cv2.waitKey()
cv2.destroyAllWindows()