a = input().split()
for n in a:
    c = a.count(n)
    if c == 1:
        print(n)
        break
        
