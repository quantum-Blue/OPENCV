import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
y = x

plt.plot(x,y,"o--")  # o, o-, o--
plt.plot(x,-y)
plt.plot(-x,y,"o")
plt.title("y=x, y=-x")
plt.show()
