import cv2
import numpy as np

image = np.ones((500,500,3), dtype=np.uint8)*255

image[0:50,0:50] = [0,0,0]
image[0:50,450:500] = [255,0,0]
image[450:500,0:50] = [0,255,0]
image[450:500,450:500] = [0,0,255]

cv2.imshow("Boxes", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
