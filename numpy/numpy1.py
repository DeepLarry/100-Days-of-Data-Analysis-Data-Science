import numpy as np
a=np.array([[1,2,3,4]])
print(a.ndim)



a=np.array([[1,2,3,],[4,5,6]])
print(a.shape)

print(a.size)

arr=np.array([1,2,3],ndmin=2)
print(arr.ndim)

a1=np.zeros((3,3))
print(a1)

a1=np.ones((3,3),dtype='i4')
print(a1.dtype)

a1=np.full((3,3),7)
print(a1)

a1=np.arange(5,50,5)
print(a1.reshape(3,3))
print(a1)

a1=np.identity(3,dtype='i4')
print(a1)


import random
a2=random.randint(3,4)
print(a2)

import numpy as np

a = np.array([1,2,3,4])
print(type(a))

import numpy as np

a = np.arange(1,6)
print(a)

import numpy as np

a = np.array([1,2,3,4,5,6])

print(a[2:5])