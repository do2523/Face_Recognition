import cv2

video = cv2.VideoCapture(0) # internal webcam = 0  external webcam = 1
faces = cv2.CascadeClassifier('./data/harcasscade.xml')

while True:
    ret, frame = video.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()