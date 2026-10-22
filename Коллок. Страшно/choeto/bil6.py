"""def bs(a):
    n = len(a)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break"""

"""def sort(a):
    n = len(a)
    for i in range(n):
        key = a[i]
        j = i-1
        while j>= 0 and a[j]>key:
            a[j+1] = a[j]
            j-=1
        a[j+1]=key
    return a
a = [5,2,4,1]
print(sort(a))"""

"""def sort(a):
    n = len(a)
    for i in range(n-1):
        m = i
        for j in range(i+1,n):
            if a[j] < a[m]:
                m=j
        a[i],a[m] = a[m], a[i]
    return a
a = [5,2,4,1]
print(sort(a))"""