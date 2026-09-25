a = input().split()
max = 0
for n in a:
    c = a.count(n)
    if c > max:
        max = c
        maxn = n
print(maxn)
        