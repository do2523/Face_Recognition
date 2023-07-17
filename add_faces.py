import cv2

video = cv2.VideoCapture(0) # internal webcam = 0  external webcam = 1

while True:
    ret, frame = video.read()
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()