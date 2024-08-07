import numpy as np
import matplotlib.pyplot as plt

path = 'D:\\temp\\OpenCV\\test_images\\smile.jpg'
img = plt.imread(path)
print(img)
print("min value: ",img.min())
print("max value: ", img.max())
print("mean: ", img.mean())
print("median: ",np.median(img))
print("average: ",np.average(img))
print("mean1: ",np.mean(img))
