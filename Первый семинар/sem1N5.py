N, b, c = input().split()
b = int(b)
c = int(c)

val = 0
for i in range(len(N)):
    val += int(N[-i-1]) * b**i

res = ""
while(val>0):
    res += str(val%c)
    val = val // c


print(res[::-1])