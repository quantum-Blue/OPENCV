# PLAKA OKUMA
# Çalışmıyor
import cv2
import numpy as np
import pytesseract
import imutils

#img=cv2.imread("plaka.png")
img=cv2.imread("plaka1.jpeg")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
filtre=cv2.bilateralFilter(gri,7,200,200)

kose=cv2.Canny(filtre,40,200)
#kose1=cv2.Canny(gri,40,200)# gorme amaclı

kontur,a=cv2.findContours(kose,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt=imutils.grab_contours((kontur,a))
cnt=sorted(cnt,key=cv2.contourArea,reverse=True)[:10]
ekran=0

for i in cnt:
    eps=0.018*cv2.arcLength(i,True)
    aprx=cv2.approxPolyDP(i,eps,True)
    if len(aprx)==4:
        ekran=aprx
        break

maske=np.zeros(gri.shape,np.uint8)
yenimaske=cv2.drawContours(maske,[ekran],0,(255,255,255),-1)
yazi=cv2.bitwise_and(img,img,mask=maske)

(x,y)=np.where(maske==255)
(ustx,usty)=(np.max(x),np.max(y))
(altx,alty)=(np.min(x),np.min(y))

kirp=gri[ustx:altx+1,usty:alty+1]

text=pytesseract.image_to_string(kirp,lang="eng")
print(text)

#cv2.imshow("1",img)
cv2.imshow("2",gri)
#cv2.imshow("3",filtre)
#cv2.imshow("4",kose)
#cv2.imshow("5",kose1)
#cv2.imshow("6",yenimaske)
cv2.imshow("7",yazi)
cv2.imshow("8",kirp)


cv2.waitKey(0)
cv2.destroyAllWindows(img)




