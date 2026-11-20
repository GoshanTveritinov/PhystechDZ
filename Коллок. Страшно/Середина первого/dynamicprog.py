#4, 7 - 11 Билеты

import numpy as np

def livenshtain_distance(word1, word2):
    len1, len2 = len(word1), len(word2)
    dp = [ [0]* (len2 + 1) for _ in range(len1 + 1) ]

    for i in range(len1 +1):
        dp[i][0] = i
    for j in  range(len2 +1):
        dp[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            dp[i][j] = min( dp[i-1][j] +1 , dp[i][j-1] +1, dp[i-1][j-1] + (word1[i-1] != word2[j-1] ))

    return dp[len1][len2]

#print(livenshtain_distance("qwer", "wer"))

a1 = "qwertyu"
a2 = "zxcrb"
d = np.array(livenshtain_distance(a1, a2))
#print( d)

def lcs(a, b):
    dp = [[0]*(len(b)+1) for _ in range(len(a)+1) ]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max( dp[i][j-1], dp[i-1][j]  )

    res = []
    i, j =len(a), len(b)
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            res.append(a[i-1])
            i -= 1
            j -= 1
        else:
            if dp[i][j-1] > dp[i-1][j]:
                j -=1
            else:
                i -=1
    return dp #[len(a)][len(b)], res[::-1]

X = "abcabaac"
Y = "baccbca"
#print(np.array(lcs(X, Y)))

def lis(a):
    dp = []
    pos = []
    prev = [-1]*len(a)

    for i,x in  enumerate(a):
        left, right = 0, len(dp)

        while left < right:         #
            mid = (left + right)//2 #
            if dp[mid] < x:         #
                left = mid+1        # Бинарный поиск, смотрим, куда поставить новый элемент
            else:                   #
                right = mid         #

        j = left
        if j >0:
            prev[i] = pos[j-1]

        if j == len(dp):
            dp.append(x)
            pos.append(i)
        else:
            dp[j] = x
            pos[j] = i

    ans = []
    if pos:
        p = pos[-1]
        while p != -1:
            ans.append(a[p])
            p = prev[p]

    return dp, ans[::-1]

#print(lis([3,4,5, 1,2]))

def backpack(weights, values, capacity):
    #Возвращает:
    #- максимальную стоимость;
    #- номера выбранных предметов, начиная с 1.
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]
        for c in range(capacity + 1):
            # Вариант 1: не брать текущий предмет.
            dp[i][c] = dp[i - 1][c]
            # Вариант 2: взять, если хватает вместимости.
            if weight <= c:
                candidate = value + dp[i - 1][c - weight]
                dp[i][c] = max(dp[i][c], candidate)

    # Восстановление одного из оптимальных наборов.
    selected = []
    c = capacity
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            selected.append(i)
            c -= weights[i - 1]
    selected.reverse()
    return dp[n][capacity], selected
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

best_value, selected = backpack(weights, values, capacity)
total_weight = sum(weights[i - 1] for i in selected)
print("Максимальная стоимость:", best_value)
print("Номера предметов:", selected)
print("Общий вес:", total_weight)

#print(np.array(backpack(weights, values, capacity)))