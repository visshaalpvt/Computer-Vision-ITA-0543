import cv2

image = cv2.imread("sample.jpg",0)

sobelx = cv2.Sobel(image, cv2.CV_64F,1,0,ksize=3)

sobely = cv2.Sobel(image, cv2.CV_64F,0,1,ksize=3)

cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()