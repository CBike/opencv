import cv2

bike = cv2.imread('./image/S1000rr.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('bike',bike)
k = cv2.waitKey(0)
# k = cv2.waitKey(0) & 0xFF
if k ==27 :
    cv2.destroyAllWindows()

elif k == ord('s'):
    cv2.imwrite('./image/S1000rr_grayscale.jpg', bike)
    cv2.destroyAllWindows()