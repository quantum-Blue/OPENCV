import numpy as np

x = np.empty([3,3],np.uint8)
print("x: ",x)
print("-------")

y = np.full((3,3,3),dtype=np.int16,fill_value=10)
print("y: ",y)
print("-------")

z = np.ones((2,5,5),dtype=np.int8)
print("z: ",z)

j = np.zeros((2,3,3),dtype=np.int8)
print("j: ",j)
