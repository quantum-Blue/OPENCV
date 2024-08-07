import numpy as np

x = np.array([[1,2,3],[4,5,6]],np.int16)
print(x)

print("-----")
print(x[0]);print(x[0,0]);print(x[0,1]);print(x[0,2])
print("-----")
print(x[1]);print(x[1,0]);print(x[1,1]);print(x[1,2])

print(x[:,0]);print(x[:,1]);print(x[:,2])
print("-----")
print(x[0,:]);print(x[1,:])

