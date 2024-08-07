# dış bükey tespit
import cv2
import numpy as np

"""
img = cv2.imread("star.png")

gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gri, 75, 200, cv2.THRESH_BINARY)
contur, h = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(contur) # degerleri matrix de gosterir

h = []  # Dış bükey çekirdekleri saklayacak liste

for i in range(len(contur)):
    hull = cv2.convexHull(contur[i], False)
    h.append(hull)

z = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

for i in range(len(contur)):
    cv2.drawContours(z, contur, i, (255, 0, 0), 3, 8)
    cv2.drawContours(z, h, i, (0, 255, 0), 1, 8)
    # 3 çizgi kalınlığı, 8 çizginin düz ve sğrekli olması için

cv2.imshow("resim", z)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# ALAN , CEVRE HESAPLAMA

img = cv2.imread("star.png")

gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
a, thresh = cv2.threshold(gri, 125, 255, cv2.THRESH_BINARY)
contur, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull=[]


for i in range(len(contur)):
    hull.append(cv2.convexHull(contur[i], False))

tuval=np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)

for i in range(len(contur)):
    cv2.drawContours(tuval, contur, i, (255, 0, 0), 3, 8, hier)
    cv2.drawContours(tuval, hull, i, (0, 255, 0), 1, 8)

cnt = hull[0]
print("cnt : " , cnt )
M = cv2.moments(cnt)
print("M : " , M)

alan = cv2.contourArea(cnt)
print("alan : " , alan)
print( "M['m00'] : " , M['m00'])

cevre = cv2.arcLength(cnt,True)
print("cevre : " , cevre)

cv2.imshow("a", tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()

