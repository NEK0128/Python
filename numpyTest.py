import numpy as np

N = 100
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8 , 9], [10, 11, 12]])
print(a)
print(a.flags)
print(a.ndim)
b = np.ones([N, 5])
print(b)


print(np.identity(3))
