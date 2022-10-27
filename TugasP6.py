import cv2

capture = cv2.VideoCapture(0)

while(True) :

    _ , frame = capture.read()

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    wajah = face_cascade.detectMultiScale(
        frame,
        scaleFactor = 1.5,
        minNeighbors = 2
    )

    for x, y, w, h in wajah:
        frame = cv2.rectangle(
            frame,
            (x,y),
            (x+w, y+h),
            (0, 255, 0),
            3
        )

    cv2.imshow('Face', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

capture.realease()
cv2.destroyAllWindows()