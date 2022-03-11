import cv2
import time

bike = cv2.imread('./image/S1000rr.jpg')
bike = cv2.resize(bike, dsize=(600,400), interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(bike, cv2.COLOR_BGR2GRAY)
height, width = gray.shape

th = 150


# for i in range(height):
#     for j in range(width):
#         if grey[i][j] > th:
#             grey[i][j] = 255
#         else:
#             grey[i][j] = 0

# inRange
# gray = cv2.inRange(gray, th, 255)


# threshold
# gray = cv2.threshold(gray)


flag = [cv2.THRESH_BINARY, cv2.THRESH_MASK, cv2.THRESH_TOZERO, cv2.THRESH_TRUNC,
        cv2.THRESH_BINARY_INV, cv2.THRESH_TOZERO_INV, cv2.THRESH_TRIANGLE, cv2.THRESH_OTSU]

flag_names = ['cv2.THRESH_BINARY', 'cv2.THRESH_MASK', 'cv2.THRESH_TOZERO', 'cv2.THRESH_TRUNC',
             'cv2.THRESH_BINARY_INV', 'cv2.THRESH_TOZERO_INV', 'cv2.THRESH_TRIANGLE', 'cv2.THRESH_OTSU']


cv2.imshow('bike',bike)
cv2.imshow('greyscale',gray)


for n, i in enumerate(flag):
    start = time.perf_counter()
    ret , result = cv2.threshold(gray, th, 255, i)
    finish = time.perf_counter()
    print(finish - start)
    print('threshold',ret)
    cv2.imshow('{0}'.format(flag_names[n]), result)
cv2.waitKey()
