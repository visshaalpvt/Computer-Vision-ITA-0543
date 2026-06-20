import cv2

face = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

image = cv2.imread("face.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face.detectMultiScale(gray,1.1,4)

print("Number of faces:", len(faces))

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Faces", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
