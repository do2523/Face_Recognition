import cv2

video = cv2.VideoCapture(0) # internal webcam = 0  external webcam = 1
face_detect = cv2.CascadeClassifier('./data/harcasscade.xml')

faces_data = []

faces_data = []

i = 0
while True:
    ret, frame = video.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detect.detectMultiScale(gray_scale, 1.3, 5)
    for (x,y,w,h) in faces:
        crop_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50,50))
        if len(faces_data) <= 100 and i %10 == 0:
            faces_data.append(resized_img)
        i += 1
        cv2.putText(frame, str(len(faces_data)), (50,50), cv2.FONT_HERSHEY_TRIPLEX, 1, (50,50,255), 1 )
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255),3)
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q') or len(faces_data) == 100:
        break
video.release()
cv2.destroyAllWindows()