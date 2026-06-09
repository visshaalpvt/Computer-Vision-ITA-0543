import cv2

image = cv2.imread("sample.jpg")

rotated = cv2.rotate(image, cv2.ROTATE_180)

cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()