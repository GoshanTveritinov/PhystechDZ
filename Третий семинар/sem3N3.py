a, b = map(int, input().split())

def d(a, b):
    #a = max, b = min
    a, b = max(a,b), min(a,b)
    while a != b:
        a, b = max(a-b, b), min (a-b, b)
    else:
        d = a
        return d

def xyA(a, b):
    x = 1
    y = 0
    while a*x + b*y != d(a, b):
        y = 0
        x -= 1
        while a*x + b*y < d(a,b):
            y += 1
    else:
        xyA = [x, y]
    return xyA

def xyB(a, b):
    x = 1
    y = 0
    while (a*y + b*x) != d(a,b):
        y = 0
        x -= 1
        while (a*y + b*x) < d(a,b):
            y += 1
    else:
        xyB = [x, y]
        return xyB

if a == b:
    xy = [0,1]
else:
    if abs(xyA(a,b)[0]) + abs(xyA(a,b)[1]) < abs(xyB(a,b)[0]) + abs(xyB(a,b)[1]):
        xy = xyA(a,b)
    elif abs(xyA(a,b)[0]) + abs(xyA(a,b)[1]) > abs(xyB(a,b)[0]) + abs(xyB(a,b)[1]):
        xy = xyB(a,b)
    else:
        if xyA(a,b)[0] < xyB(a,b)[0]:
            xy = xyA(a,b)
        else:
            xy = xyB(a,b)



print(xy[0], xy[1], d(a,b))