import numpy as np

N, M = map(int, input().split())
l = N*M
a = np.zeros((N, M))
for n in range(N):
    stroka = list(map(int, input().split()))
    for m in range(M):
        a[n][m] = stroka[m]


def dets(A):
    m = A.shape[1]
    b = A[:, m-1:m]
    x = A[:, :m-1]
    dets = [int(round(np.linalg.det(x), 2))]
    for i in range (m-1):
        D = np.hstack( (x[:, :i], b, x[:, i+1:m-1]) )
        dets += [int(round(np.linalg.det(D), 2))]
    return(dets)

if dets(a)[0] == 0:
    print("Система уроавнений не имеет решений вообще или имеет бесконечно многт решений")
else:
    answers = {}
    for i in range(1, len(dets(a))):
        answers['x'+str(i)] = dets(a)[i] / dets(a)[0]
    print(answers)