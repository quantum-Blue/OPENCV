import cv2
import numpy as np

def fonx(x):
    pass

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow("image")

cv2.createTrackbar("r","image",0,255,fonx)
cv2.createTrackbar("g","image",0,255,fonx)
cv2.createTrackbar("b","image",0,255,fonx)

switch="Switch"
cv2.createTrackbar("switch","image",0,1,fonx)

while True:
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

    r=cv2.getTrackbarPos("r","image")
    g=cv2.getTrackbarPos("g","image")
    b=cv2.getTrackbarPos("b","image")

    img[:]=[b,g,r]

    s=cv2.getTrackbarPos(switch,"image")
    
    if s==0:
        img[:]=[0,0,0]

    elif s==1:
        img[:]=[b,g,r]


cv2.waitKey(0)
cv2.destroyAllWindows()

