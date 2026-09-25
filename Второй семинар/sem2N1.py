A = list(map(int, input().split()))

l = A[0]
numbers = A[1::]
lost = 0

for i in range(l):
    a = i+1
    for n in numbers:
        res = a ^ n
        if res == 0:
            lost = 0
            break
        lost = a
    if lost != 0:
        break


print(lost)
