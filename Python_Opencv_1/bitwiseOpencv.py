import cv2
import numpy as np

img1=cv2.imread("rei.png")
img2=cv2.imread("akeno.png")

bit_and=cv2.bitwise_and(img1,img2)
bit_not1=cv2.bitwise_not(img1,img2)
bit_not2=cv2.bitwise_not(img2,img1)


cv2.imshow("bir",img1)
cv2.imshow("iki",img2)
cv2.imshow("and",bit_and)
cv2.imshow("not1",bit_not1)
cv2.imshow("not2",bit_not2)

cv2.waitKey(0)
cv2.destroyAllWindows()

