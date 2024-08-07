import cv2

img=cv2.imread("resim2.jpg")
yuz=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=yuz.detectMultiScale(gri,1.3,4) #1.3 : ölçeklendirme,4:kaç çerçeve olacağı

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()






