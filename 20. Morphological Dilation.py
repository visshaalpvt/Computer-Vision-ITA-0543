import cv2
import numpy as np

image = cv2.imread("sample.jpg",0)

kernel = np.ones((5,5), np.uint8)

dilation = cv2.dilate(image,kernel)

cv2.imshow("Dilation", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()