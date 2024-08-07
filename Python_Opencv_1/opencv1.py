import cv2
#import numpy
#import matplotlib

#img = cv2.imread("rei.png")
#print(img) # matrixlerle pikselleri belirtir
img = cv2.imread("rei.png",cv2.IMREAD_GRAYSCALE) # resmi gri tonlarında gosterir
#img = cv2.imread("rei.png",0) # usttekiyle ayni sey
img = cv2.resize(img,(400,300))
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",img)
cv2.imwrite("copy.png",img) # img deki verileri copy.png olarak kopyalayıp kaydeder
cv2.waitKey(0) # klavyeden tusa basana kadar kapanmaz
#cv2.waitKey(500) # 500 milisaniye acik kalip kapanir(0.5 saniye)

cv2.destroyAllWindows()
