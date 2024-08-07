import cv2

img=cv2.imread("rei.png")
sat,sut=img.shape
#print(sut) # sutunun kaç pixelden olustugunu gosterir
#print(sat) # satirin kaç pixelden olustugunu gosterir
sat,sut=img.shape
m=cv2.getRotationMatrix2D((sut/2,sat/2),180,1) 
# boldukce resim kuculuyı (kesiliyo),180 çevrilme derecesi,sondaki bir yaklastirma icim
d=cv2.warpAffine(img,m,(sut,sat))


cv2.imshow("resim",d)
cv2.waitKey(0)
cv2.destroyAllWindows()

