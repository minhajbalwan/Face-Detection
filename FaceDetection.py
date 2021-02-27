import cv2

trainer_face_data = cv2.CascadeClassifier("C:\\Users\\balwa\\OneDrive\\Desktop\\Minhaj\\Projects\\AI\\haarcascade_frontalface_default.xml")

webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read, frame = webcam.read()
    grayscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trainer_face_data.detectMultiScale(grayscaled_image)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 256, 0), 2)
    cv2.imshow("Face", frame)
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break