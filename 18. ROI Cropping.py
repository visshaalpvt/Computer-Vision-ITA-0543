import cv2

image = cv2.imread("sample.jpg")

roi = image[100:300,100:300]

cv2.imshow("ROI", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()