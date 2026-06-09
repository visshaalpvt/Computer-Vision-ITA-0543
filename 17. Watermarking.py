import cv2

image = cv2.imread("sample.jpg")

watermark = image.copy()

cv2.putText(watermark,"SAVEETHA",(50,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,(255,255,255),2)

cv2.imshow("Watermarked", watermark)

cv2.waitKey(0)
cv2.destroyAllWindows()