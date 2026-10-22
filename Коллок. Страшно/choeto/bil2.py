"""def bin(a,x):
    N = len(a)
    if N==0:
        return False
    if N == 1:
        return a[0] == x
    if x == a[N]:
        return N
    mid = N//2
    if x < a[mid]:
        return bin(a[:mid],x)
    if x > a[mid]:
        return bin(a[mid+1:],x)
    """
"""`def bin(a,x,left,right):
    N = len(a)
    if left>right:
        return False
    mid = (right+left)//2
    if x == a[mid]:
        return x == a[mid]
    elif x>a[mid]:
        return bin(a,x,mid+1,right)
    else: return bin(a,x,left,mid-1)`"""
