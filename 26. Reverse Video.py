import cv2

cap = cv2.VideoCapture("video.mp4")

frames = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

frames.reverse()

height,width,layers = frames[0].shape

out = cv2.VideoWriter("reverse.mp4",
                      cv2.VideoWriter_fourcc(*'mp4v'),
                      30,
                      (width,height))

for frame in frames:
    out.write(frame)

out.release()
cap.release()
