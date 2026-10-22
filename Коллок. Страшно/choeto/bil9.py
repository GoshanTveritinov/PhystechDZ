def lis(n,a):
    d = [1]*n
    for i in range(1,n):
        for j in range(i):
            if a[j] < a[i]:
                d[i] = max(d[i],d[j]+1)
    return d
n = int(input())
a = list(map(int, input().split()))
print(lis(n, a))