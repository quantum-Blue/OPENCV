import numpy as np
import matplotlib.pyplot as plt

"""
N = 11
x = np.linspace(0,10,N)

y = x

plt.plot(x,y,"o--")
plt.axis("off")
plt.show()
"""

x = [1,2,3,4]
plt.plot(x,[y**2 for y in x])
plt.show()
