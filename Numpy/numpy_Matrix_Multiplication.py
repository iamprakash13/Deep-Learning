import numpy as np

## Element-Wise Multiplication

m = np.array([[1,2,3],[4,5,6]])
m
# displays the following result:
# array([[1, 2, 3],
#        [4, 5, 6]])

n = m * 0.25
n
# displays the following result:
# array([[ 0.25,  0.5 ,  0.75],
#        [ 1.  ,  1.25,  1.5 ]])

m * n
# displays the following result:
# array([[ 0.25,  1.  ,  2.25],
#        [ 4.  ,  6.25,  9.  ]])

np.multiply(m, n)   # equivalent to m * n
# displays the following result:
# array([[ 0.25,  1.  ,  2.25],
#        [ 4.  ,  6.25,  9.  ]])


## Matrix Product (dot product)

a = np.array([[1,2,3,4],[5,6,7,8]])
a
# displays the following result:
# array([[1, 2, 3, 4],
#        [5, 6, 7, 8]])
a.shape
# displays the following result:
# (2, 4)

b = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b
# displays the following result:
# array([[ 1,  2,  3],
#        [ 4,  5,  6],
#        [ 7,  8,  9],
#        [10, 11, 12]])
b.shape
# displays the following result:
# (4, 3)

c = np.matmul(a, b)
c
# displays the following result:
# array([[ 70,  80,  90],
#        [158, 184, 210]])
c.shape
# displays the following result:
# (2, 3)
'''
If your matrices have incompatible shapes, you'll get an error, like the following:

np.matmul(b, a)
# displays the following error:
# ValueError: shapes (4,3) and (2,4) not aligned: 3 (dim 1) != 2 (dim 0)
'''


## NumPy's dot function

a = np.array([[1,2],[3,4]])
a
# displays the following result:
# array([[1, 2],
#        [3, 4]])

np.dot(a,a)
# displays the following result:
# array([[ 7, 10],
#        [15, 22]])

a.dot(a)  # you can call `dot` directly on the `ndarray`
# displays the following result:
# array([[ 7, 10],
#        [15, 22]])

np.matmul(a,a)
# array([[ 7, 10],
#        [15, 22]])

