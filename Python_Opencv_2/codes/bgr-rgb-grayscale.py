import cv2
import matplotlib.pyplot as plt

path = "D:\\temp\\OpenCV\\test_images\\smile.jpg"
img = cv2.imread(path,0) # BGR
#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(img,cmap='gray',interpolation = 'BICUBIC') # RGB
plt.show()
