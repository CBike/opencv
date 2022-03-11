import cv2
import matplotlib.pyplot as plt

ferret = cv2.imread('./image/ferret.jpg')
cat = cv2.imread('./image/cat.jpg')
cv2.cvtColor(ferret, cv2.COLOR_BGR2RGB, dst=ferret)

cv2.imshow('test',ferret)
cv2.waitKey()