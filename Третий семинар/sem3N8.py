import random as rd
N = int(input())
X = [rd.gauss(0, 50) for i in range(N)]
Y = [rd.gauss(0, 50) for i in range(N)]

sq = [i**2 for i in X]
xy = [X[i]*Y[i] for i in range(N)]

def E(Q):
    q = sum(Q) / len(Q)
    return q

def kb(X, Y):
    k = (E(xy)- E(X)*E(Y)) / (E(sq) - E(X)**2 )
    b = E(Y) - k*(E(X))
    kb = [k, b]
    return kb

print(f'Получается прямая с k = {round(kb(X, Y)[0], 4)} и b = {round(kb(X, Y)[1], 4)}')