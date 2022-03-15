import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)
img = cv2.ellipse(img,(256,256),(100,100),0,0,270,(0,255,0),1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()