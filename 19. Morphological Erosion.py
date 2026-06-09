import cv2
import numpy as np

image = cv2.imread("sample.jpg",0)

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(image,kernel)

cv2.imshow("Erosion", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()