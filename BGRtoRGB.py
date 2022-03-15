import cv2
from matplotlib import pyplot as plt

bike = cv2.imread('./image/S1000rr.jpg', cv2.IMREAD_COLOR)

rgbbike = cv2.cvtColor(bike,cv2.COLOR_BGR2RGB)

plt.imshow(rgbbike)
plt.xticks([])
plt.yticks([])
plt.show()
