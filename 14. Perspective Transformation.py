import cv2
import numpy as np

image = cv2.imread("sample.jpg")

rows, cols, ch = image.shape

pts1 = np.float32([[50,50],[300,50],[50,300],[300,300]])
pts2 = np.float32([[10,100],[250,50],[100,250],[300,300]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

output = cv2.warpPerspective(image, matrix, (cols, rows))

cv2.imshow("Perspective", output)

cv2.waitKey(0)
cv2.destroyAllWindows()