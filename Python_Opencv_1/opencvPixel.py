import cv2
import numpy as np

img=cv2.imread("rei.png")

# renk=img[200,300]
# print(renk)
#print(img.shape) # resmin boyutlarını verir
# mavi=img[200,300,0] # renklerin her birinin ne kadar kullanıldığı
# print("mavi",mavi)
# yesil=img[200,300,1]
# print("yesil",yesil)
# kirmizi=img[200,300,2]
# print("kirmizi",kirmizi)


img[200,300,0]=0
print(img[200,300,0])

mavi = img.item(150,150,0)
print(mavi)
img.itemset((150,150,0),200)
print(img[150,150])


cv2.imshow("REI",img)

cv2.waitKey(0)
cv2.destroyAllWindows()





