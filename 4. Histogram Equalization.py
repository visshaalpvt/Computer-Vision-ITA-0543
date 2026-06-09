import cv2

image = cv2.imread("sample.jpg",0)

equalized = cv2.equalizeHist(image)

cv2.imshow("Original", image)
cv2.imshow("Equalized", equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()