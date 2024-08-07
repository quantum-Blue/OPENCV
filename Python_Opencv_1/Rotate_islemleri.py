import cv2


cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
# 0 verirsek 180 derece çevirir , -1 aynı şekide 
    frame=cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
# 90 derece sola çevirir
# bunun gibi var bikaç tane bunlar rotate işlemleri 

    cv2.imshow("asd",frame)
    if cv2.waitKey(5) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()






