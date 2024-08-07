import numpy as np
import matplotlib.pyplot as plt

x = np.arange(3)

plt.plot(x,[y**2 for y in x])
plt.plot(x,[y**3 for y in x])
plt.plot(x,2*x)
plt.plot(x, 5.2*x)
plt.legend(['x**2','x**3','x*2','x*5.2'],loc='lower right') # upper right/center/left, lower right/center/left
plt.grid(True)
plt.xlabel('x = np.arange(3)')
plt.ylabel('y = f(x)')
plt.axis([0,2,0,10])
plt.title("Simple Plot")
plt.savefig('D:\\temp\\OpenCV\\plt.png')

plt.show()
