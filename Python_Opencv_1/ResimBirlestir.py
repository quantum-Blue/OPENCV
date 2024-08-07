import cv2
import numpy as np

daire=np.zeros((512,512,3),np.uint8)+225
cv2.circle(daire,(256,256),50,(255,0,0),-1)

kare=np.zeros((512,512,3),np.uint8)+225
cv2.rectangle(kare,(150,150),(350,350),(0,255,0),-1)

agirlik=cv2.addWeighted(daire,0.6,kare,0.4,0)

cv2.imshow("agirlik",agirlik)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 2 resim birleştirilirken aynı pixelde olmaları gerekir