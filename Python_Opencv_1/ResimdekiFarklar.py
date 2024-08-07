import cv2
#import numpy as np
img1=cv2.imread("rei.png")
img2=cv2.imread("rei1.png")

fark=cv2.subtract(img1,img2)
b,g,r=cv2.split(fark)
print(fark)

cv2.imshow("1",fark)

"""
cv2.imshow("1",img1)
cv2.imshow("2",img2)
"""

cv2.waitKey(0)
cv2.destroyAllWindows()

