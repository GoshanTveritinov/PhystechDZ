n = int(input())

def fib(N, cache = {0:0, 1:1} ):
    if N in cache:
        return cache[N]
    else:
        cache[N] = fib(N-1, cache) + fib(N-2, cache)
        return cache[N]

print(fib(n))
