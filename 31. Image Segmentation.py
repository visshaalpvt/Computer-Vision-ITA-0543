import cv2

image = cv2.imread("sample.jpg",0)

ret, thresh = cv2.threshold(image,127,255,
                            cv2.THRESH_BINARY)

cv2.imshow("Segmented", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
