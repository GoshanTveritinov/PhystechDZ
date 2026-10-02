import numpy as np

a = np.arange(12).reshape((3, 4))
print(a)
print()
#[[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]
#print(a[:, 1])
# [1 5 9]

x = np.arange(3)
#a[:, 1] = x
#print(a)

b = a[:, 3:4]
c = a[:, 3]
print(b)
print(c)
print()

s = a.shape
i = 0
D = np.hstack( (a[:, :i], b, a[:, i+1:s[1]-1]) )

print(D)
print(np.linalg.det(D))

print(s[0], s[1])