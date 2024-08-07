import numpy as np
import matplotlib.pyplot as plt

path = 'D:\\temp\\OpenCV\\test_images\\coins.jpg'
img = plt.imread(path)
print(img);print("type: ",type(img));print("shape: ",img.shape);print("ndim: ",img.ndim);print("size: ",img.size);print("dtype:", img.dtype)

print("red channel: ",img[50,50,0]) # rgb--> r =0, g=1, b=2
print("green channel: ",img[50,50,1])
print("blue channel: ",img[50,50,2])
print("rgb channel value: ",img[50,50,:])
