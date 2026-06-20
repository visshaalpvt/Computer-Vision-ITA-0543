import cv2

watch_cascade = cv2.CascadeClassifier("watch.xml")

image = cv2.imread("watch.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

watch = watch_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in watch:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Watch Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
