
import cv2
import numpy as np

img=cv2.imread("rei.png") # siyah beyaz resim daha iyi olur
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(gri,100,200,cv2.THRESH_BINARY)
cont,a=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print(cont)

cv2.drawContours(img,cont,-1,(0,255,0),2)


cv2.imshow("1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()









