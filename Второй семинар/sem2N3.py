G = input()

ml = ["A", "H", "I", "M", 'O', 'T', 'U', 'V', 'W', 'X', 'Y', 1, 8]
aml = ["E", 'J', 'S', 'Z']  
bml = ["3", 'L', '2', '5']
all = ml + aml + bml
type = 0


for i in range(len(G)//2 + 1):
    type = 0
    letter = G[i]
    j = -i-1

    if letter not in all:
        break
    elif letter in ml:
        check = G[i] == G[j]
        if int(check) == 0:
            break
    elif letter in aml:
        n = aml.index(letter)
        Mletter = bml[n]
        check = Mletter == G[j]
        if int(check) == 0:
            break
    elif letter in bml:
        n = bml.index(letter)
        Mletter = aml[n]
        check = Mletter == G[j]
        if int(check) == 0:
            break  
    type = 1  

if G == G[::-1]:
    type += 2

result = {0: "is not a palindrome.", 1: "is a mirrored string.", 2: "is a regular palindrome.", 3: "is a mirrored palindrome."}

print(f'{G} {result[type]}')
