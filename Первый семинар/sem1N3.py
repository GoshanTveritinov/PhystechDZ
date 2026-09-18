a = list(map(int, input().split()))
n = len(a)
p = 1
for i in a:
    p = p*i
geom = p ** (1/n)
print(geom)