import cv2
import numpy as np

img = cv2.imread("/Users/enesbal/Desktop/UdemyOpencv/photo/helikopter2.jpg",0)

kernel = np.ones((5,5),np.uint8)
tophat = cv2.morphologyEx(img,cv2.MORPHOLOGY_TOPHAT,kernel)

cv2.imshow("img",img)
cv2.imshow("TOPHAT",tophat)
