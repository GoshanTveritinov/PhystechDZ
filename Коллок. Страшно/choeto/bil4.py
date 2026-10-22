"""def grasshopper(price,n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = price[1]
    for i in range(2, n+1):
        dp[i] = min(price[i-1],price[i-2])+price[i]
    return dp[n]
"""

"""def g(price,n):
    dp = [0]*(n+1)
    prev = [0]*(n+1)
    dp[1] = price[1]
    for i in range(2, n+1):
        if dp[i-1]<dp[i-2]:
            prev[i] = dp[i-1]
        else: prev[i] = dp[i-2]
        dp[i] = dp[prev[i]] + price[i]
    path = []
    i = n
    while i != 0:
        path.append(i)
        i = prev[i]
    path.append(0)
    path.reverse()
    return dp[n],path"""









def g(price, n):
    dp = [0]*(n+1)
    prev = [0]*(n+1)
    dp[1]=price[1]
    for i in range(2,n+1):
        if dp[i-1] < dp[i-2]:
            prev[i] = dp[i-1]
        else: prev[i] = prev[i-2]
        dp[i] = dp[prev[i]]+price[i]
    path = []
    i = n
    while i>0:
        path.append(i)
        i = prev[i]
    path = path.reverse
    return dp[n], path
n = 5
price = [0, 3, 2, 5, 1, 4]
print(g(n,price))





















