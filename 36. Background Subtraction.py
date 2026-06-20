import cv2

cap = cv2.VideoCapture("video.mp4")

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    fgmask = fgbg.apply(frame)

    cv2.imshow("Background Subtraction", fgmask)

    if cv2.waitKey(30)==27:
        break

cap.release()
cv2.destroyAllWindows()
