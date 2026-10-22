def l(s1,s2):
    n = len(s1)
    m = len(s2)
    if n > m:
        s1,s2 = s2, s1
        n,m = m, n
    current_row = range(n+1)
    for i in range(1,m+1):
        previous_row, current_row = current_row, [i]+[0]*n
        for j in range(1,n+1):
            add = previous_row[j]+1
            remove = current_row[j-1]+1
            change = previous_row[j-1]
            if s1[j-1]!=s2[i-1]:
                change += 1
            current_row[j] = min(add,remove,change)
    return current_row[n]
