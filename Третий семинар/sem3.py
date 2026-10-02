import numpy as np

def f(x=[]):
    x.append(1)
    print(x)

# повтори, если
#while N != 0:

A = np.arange(12).reshape((3, 4))
m = A.shape[1]
b = A[:, m-1:m]
x = A[:, :m-1]

dets = [round(np.linalg.det(x), 2)]
for i in range (m-1):
    D = np.hstack( (x[:, :i], b, x[:, i+1:m-1]) )
    dets += [int(round(np.linalg.det(D), 2))]
    #print(D)

print(dets)