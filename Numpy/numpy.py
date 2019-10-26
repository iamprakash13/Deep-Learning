# importing numpy
import numpy as np

## scalars
# create numpy scalar array 
s = np.array(5)
print(s.shape)

# scalar addition
x = s + 3
print(x)

## Vectors
v = np.array([1,2,3])
print(v[1:])

## Matrices
m = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(m.shape)

## Tensors
t = np.array([[[[1],[2]],[[3],[4]],[[5],[6]]],[[[7],[8]],\
    [[9],[10]],[[11],[12]]],[[[13],[14]],[[15],[16]],[[17],[17]]]])
print(t.shape)

## changing shapes
# converting into 1x4
v = np.array([1,2,3,4])
x = v.reshape(1,4)
print(x.shape)

# reshaping in special way
x = v[None, :]
y = v[:, None]
print(x)
print(y)

