import cv2

cap=cv2.VideoCapture("YuruyenAdamlar.mp4") # elimizde yok
yuz=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret,frame=cap.read()
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=yuz.detectMultiScale(gri,1.2,4) #1.3 : ölçeklendirme,4:kaç çerçeve olacağı

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("1",frame)

    if ret==0:
        break

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

