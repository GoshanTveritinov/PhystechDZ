N = int(input())
a = input().split()
for i in a:
    check = 0
    for j in a:
        if j > i:
            check += 1
    if check == (N//2):
        print(i)


