import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)
img = cv2.circle(img,(200,300),100,(0,255,0),3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()