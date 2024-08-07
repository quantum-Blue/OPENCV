import cv2

img=cv2.imread("resim3.jpg")

vucud=cv2.CascadeClassifier("haarcascade_fullbody.xml")

gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


bodies=vucud.detectMultiScale(gri,1.1,1)

for x1,y1,w1,h1 in bodies:
    cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(0,0,255),2)


cv2.imshow("1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()




"""
img=cv2.imread("resim3.jpg")
yuz=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
vucud=cv2.CascadeClassifier("haarcascade_fullbody.xml")

gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=yuz.detectMultiScale(gri,1.1,4) #1.1 : ölçeklendirme,4:kaç çerçeve olacağı

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    img2=img[y:y+h,x:x+w]
    gri2=gri[y:y+h,x:x+w]

    body=vucud.detectMultiScale(gri2,1.1,1)

    for x1,y1,w1,h1 in body:
        cv2.rectangle(img2,(x1,y1),(x1+w1,y1+h1),(0,0,255),2)


cv2.imshow("1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
