class Stack: #Первый зашел последний вышел
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def print(self):
        print(self.stack)

znaki = ["+", "*", "-", "/"]
line = input().split()
#[2, 3, "-", 12, 10, "-", "*", 6, 2, "/", "+"] #       
print(line)
a = Stack()

for i in line:
    try:
        q = int(i)
        a.push(q) 
        
    except ValueError:
        s1 = int(a.pop())
        s2 = int(a.pop())

        if i == znaki[0]:
            r = s2 + s1
        elif i == znaki[1]:
            r = s2 * s1
        elif i == znaki[2]:
            r = s2 - s1 
        elif i == znaki[3]:
            r = s2 / s1

        a.push(r) 
    a.print()
print(a.pop())


