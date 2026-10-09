import numpy as np
import string
prepinanie = string.punctuation

with open(r'Четвертый семинар\license.txt', 'r') as f:
    text = f.read()


textred = text.lower().replace("\n", "")

for i in range(len(textred)-100):
    if textred[i] in prepinanie:
        znak = textred[i]
        textred = textred.replace(znak, " ")

textred = list(textred.split(' '))

g = {}
for a in range(len(textred)):
    if textred[a] in g:
        g[textred[a]] = g[textred[a]] + 1
    else:
        g[textred[a]] = 1 

k = sorted(g, key = g.get, reverse = True)[1:11]
print(k)
