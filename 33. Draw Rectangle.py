import cv2
import numpy as np

image = np.ones((500,500,3), dtype=np.uint8)*255

cv2.rectangle(image,(100,100),(400,300),
              (255,0,0),3)

cv2.imshow("Rectangle", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
