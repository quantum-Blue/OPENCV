import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("D:\\OpenCV\\test_images\\map.jpeg")

plt.subplot(4,2,1)
plt.title("Original Image")
plt.imshow(img)

plt.subplot(4,2,2)
plt.title("img+img")
plt.imshow(img+img)

plt.subplot(4,2,3)
plt.title("img-img")
plt.imshow(img-img)

plt.subplot(4,2,4)
plt.title("np.flip(img,0)")
plt.imshow(np.flip(img,0)) #0,1,2

plt.subplot(4,2,5)
plt.title("np.flip(img,1)")
plt.imshow(np.flip(img,1)) #0,1,2


plt.subplot(4,2,6)
plt.title("np.flip(img,2)")
plt.imshow(np.flip(img,2)) #0,1,2

plt.subplot(4,2,7)
plt.title("np.fliplr(img)") # left to right
plt.imshow(np.fliplr(img)) 

plt.subplot(4,2,8)
plt.title("np.flipud(img)") # updown
plt.imshow(np.flipud(img)) 

plt.show()
