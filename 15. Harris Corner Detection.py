import cv2
import numpy as np

image = cv2.imread("sample.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

dst = cv2.cornerHarris(gray,2,3,0.04)

image[dst>0.01*dst.max()] = [0,0,255]

cv2.imshow("Corners", image)

cv2.waitKey(0)
cv2.destroyAllWindows()