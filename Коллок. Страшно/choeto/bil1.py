"""def f(n):
    if n ==0:
        return 
    f(n-1)
    print(n,end=" ")
    f(n-1)
    print(n,end = " ")

    """

# факторил n! = n*(n-1)!
"""
def fac(n):
    if n == 0:
        return 1
    return n*fac(n-1)"""

"""def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(n=2))"""