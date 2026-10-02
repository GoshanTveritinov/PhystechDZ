def prosto(N):
    mn = []
    for i in range(2, int(N**0.5)+1):
        while N % i == 0:
            mn += [i]
            N = N / i
    if len(mn) == 0:
        mn = [1, N]
    return mn

a = int(input())
print(prosto(a))
