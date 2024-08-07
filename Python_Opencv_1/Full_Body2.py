import cv2

cap=cv2.VideoCapture("yuruyenAdamlar.mp4") # elimizde yok
ret,frame=cap.read()

vucud=cv2.CascadeClassifier("haarcascade_fullbody.xml")

while True:
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    bodies=vucud.detectMultiScale(gri,1.1,1)

    for x1,y1,w1,h1 in bodies:
        cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),(0,0,255),2)

    cv2.imshow("1",frame)



    if cv2.waitKey(20) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
