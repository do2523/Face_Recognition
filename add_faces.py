import cv2

video = cv2.VideoCapture(0) # internal webcam = 0  external webcam = 1
face_detect = cv2.CascadeClassifier('./data/harcasscade.xml')

while True:
    ret, frame = video.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detect.detectMultiScale(gray_scale, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255),3)
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()