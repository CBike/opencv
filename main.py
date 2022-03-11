import cv2
import matplotlib.pyplot as plt

ferret = cv2.imread('./image/ferret.jpg')
cat = cv2.imread('./image/cat.jpg')

cat = cv2.resize(cat, dsize=(0,0), fx=0.5, fy=0.5,interpolation=cv2.INTER_AREA)

HSV = cv2.cvtColor(cat, cv2.COLOR_BGR2HSV)
GREY = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY)
cat2 = cv2.cvtColor(cat, cv2.COLOR_BGR2RGB)
cv2.imshow('orign',cat)
cv2.imshow('cat(RGB)',cat2)
cv2.imshow('hsv',HSV)
cv2.imshow('GREY',GREY)
cv2.waitKey()
