memo = {0:0, 1:1}

def fm(n):
    if n in memo:
        return memo[n]
    memo[n]=fm(n-1)+fm(n-2)
    return memo[n]