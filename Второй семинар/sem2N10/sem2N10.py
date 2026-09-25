with open(r'C:\Users\Георгий\Desktop\MIPT\Второй семинар\sem2N10\input.txt', 'r') as f:
    text = f.read()

glas = ["у", "е", "э", "о", "а", "ы", "я", "и", "ю"]
words = text.split()
newtext = []
for n in words:
    slogi = []
    start = 0
    for i in range(len(n)):
        letter = n[i]
        if letter in glas and n[i-1] not in glas:
            end = i
            slogi = slogi + [n[start:end+1]] + ['с'] + [ letter ]
            start = end+1

    if end+1 != len(n):
        slogi += [n[start:len(n)+1]]

    newword = ''.join(slogi)
    newtext += [newword] 
print(*newtext)
