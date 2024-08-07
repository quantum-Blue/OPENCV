import cv2

img=cv2.imread("rei.png")

roi=img[50:1000,400:680]

cv2.imshow("resim",img)
cv2.imshow("roi",roi)

cv2.waitKey(0)
cv2.destroyAllWindows()

