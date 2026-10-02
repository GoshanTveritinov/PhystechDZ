
X = [1, 2, 3]
Y = [5, 7, 9]

sq = [i**2 for i in X]
xy = [X[i]*Y[i] for i in range(len(X))]

def E(Q):
    q = sum(Q) / len(Q)
    return q

def kb(X, Y):
    k = (E(xy)- E(X)*E(Y)) / (E(sq) - E(X)**2 )
    b = E(Y) - k*(E(X))
    kb = [k, b]
    return kb

print({'k':kb(X, Y)[0], 'b': kb(X, Y)[1]})