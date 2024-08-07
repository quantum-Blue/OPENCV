import cv2

cap = cv2.VideoCapture("cars.mov")
araba = cv2.CascadeClassifier("cars.xml")

while True:
    ret, frame = cap.read()


    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = araba.detectMultiScale(gri, 1.2, 3)

    for x, y, w, h in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Video", frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
