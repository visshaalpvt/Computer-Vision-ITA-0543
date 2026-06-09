import cv2

image = cv2.imread("sample.jpg")

bigger = cv2.resize(image,None,fx=2,fy=2)

smaller = cv2.resize(image,None,fx=0.5,fy=0.5)

cv2.imshow("Big", bigger)
cv2.imshow("Small", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()