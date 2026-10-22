def kp(weights, values, W):
    n = len(weights)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        w = weights[i-1]
        v = values[i-1]
        for cap in range(1,W+1):
            if cap>=w:
                dp[i][cap] = max(dp[i][cap],dp[i-1][cap-w]+v)
            else: dp[i][cap] = dp[i-1][cap]
    taken = []
    cap = W
    for i in range(n,0,-1):
        if dp[i][cap] != dp[i-1][cap]:
            taken.append(i-1)
            cap -= weights[i-1]
    return dp[n][W], taken
w = [2, 3, 4, 5]  # веса
v = [3, 4, 5, 8]  # стоимости
W = 5             # вместимость

max_cost, items = kp(w, v, W)
print(f"Максимальная стоимость: {max_cost}")
print(f"Индексы взятых предметов: {items}")