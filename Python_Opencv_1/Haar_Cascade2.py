import cv2

cap=cv2.VideoCapture("video3.mp4") # elimizde yok
yuz=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
goz=cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
    ret,frame=cap.read()
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=yuz.detectMultiScale(gri,1.3,4) #1.3 : ölçeklendirme,4:kaç çerçeve olacağı

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        img2=frame[y:y+h,x:x+w]
        gri2=gri[y:y+h,x:x+w]

        gozler=goz.detectMultiScale(gri2)

        for x1,y1,w1,h1 in gozler:
            cv2.rectangle(img2,(x1,y1),(x1+w1,y1+h1),(0,0,255),2)

        if ret==0:
            break

    cv2.imshow("1",img2)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


