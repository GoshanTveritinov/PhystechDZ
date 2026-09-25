G,s = input().split()
G = int(G)

l = len(s) // G
print(''.join( s[i:i+l][::-1]for i in range(0,len(s), l) ))
