import cv2

image = cv2.imread("sample.jpg")

rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()