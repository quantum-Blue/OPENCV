import cv2
import numpy as np


# TUVAL OLUSTURMA
"""
canvas = np.zeros((512,512,3),dtype=np.uint8) + 255 # Beyaz pencere
#canvas = np.zeros((512,512,3),dtype=np.uint8) + 125 #gri pencere
# tuvalin boyutu 512x512 /3 kanallı(3 renkli)

print(canvas)

cv2.imshow("pencere",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# GORUNTU OLUSTURMA
"""
img = np.zeros((20,20,3),np.uint8) + 255

# img[0][0]=(0,0,0) # Mavi tonları
# img[0][1]=(50,0,0)
# img[0][2]=(100,0,0)
# img[0][3]=(150,0,0)
# img[0][4]=(200,0,0)
# img[0][5]=(250,0,0)

img[0][0]=0 # Gri tonları
img[0][1]=50 
img[0][2]=100
img[0][3]=150
img[0][4]=200
img[0][5]=250

img = cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA) #INTER_AREA hataları onleme amaclı 
 
cv2.imshow("pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# SEKİL İSLEMLERİ
"""
canvas = np.zeros((500,500,3),dtype=np.uint8) + 255 

#cv2.line(canvas,(80,120),(200,300),(0,0,225),thickness=4) #thickness:çizginin kalınlığı
#cv2.line(canvas,(400,350),(200,300),(250,0,0),8) 
#cv2.rectangle(canvas,(100,200),(300,400),(0,0,225),thickness=5) # kare/dikdörtgen içi boş
#cv2.rectangle(canvas,(100,200),(300,400),(200,50,100),thickness=-1) # kare/dikdörtgen içi dolu

#cv2.circle(canvas,(150,150),100,(50,200,250),thickness=5) # merkez,çap,renk;çember içi boş
#cv2.circle(canvas,(250,250),150,(150,50,30),thickness=-1) # daire 

#ucgen yapimi:
u1=(300,200)
u2=(100,300)
u3=(250,350)
cv2.line(canvas,u1,u2,(0,0,0),4)
cv2.line(canvas,u3,u2,(0,0,0),4)
cv2.line(canvas,u1,u3,(0,0,0),4)

cv2.imshow("pencere",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# YAZI EKLEME
"""
canvas = np.zeros((600,600,3),dtype=np.uint8) + 255 

f1=cv2.FONT_ITALIC
f2=cv2.FONT_HERSHEY_PLAIN
f3=cv2.CAP_AVFOUNDATION

cv2.putText(canvas,"merhaba",(200,200),f1,2,(255,0,0),cv2.LINE_AA)

cv2.imshow("pencere",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

