size, symb = input().split()
b = []

def f1(n, x):
    x.append(n)
    print(''.join(x))
    global b
    b = x

def f2(n, x):
    x.pop()
    print(''.join(x))

for i in range(int(size)//2+1):
    f1(symb, b)
for i in range(int(size)//2, 0, -1):
    f2(symb, b)