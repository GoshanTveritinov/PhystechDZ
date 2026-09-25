a = input().split()
a[0:-1:2], a[1::2] = a[1::2], a[0:-1:2]
print(*a)