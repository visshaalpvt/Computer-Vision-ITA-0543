import cv2
import numpy as np

image = np.ones((500,500,3), dtype=np.uint8)*255

cv2.circle(image,(250,250),100,(0,255,0),3)

cv2.imshow("Circle", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
