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

    return dp #[len1][len2]

a1 = "qwertyu"
a2 = "zxcrb"
d = np.array(livenshtain_distance(a1, a2))
#print( d)

#def lcs(a, b):
#    dp = 

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

print(lis([3,4,5, 1,2]))


