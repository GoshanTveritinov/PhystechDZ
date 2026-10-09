class Cat:
    def __init__(self, breed1, color, age):
        self.breed = breed1
        self.color = color
        self.age = age
    def meow(self):
        print("Meow")


c = Cat("Russian white", 'balck', 10)
print(c.breed)
c.meow()
Cat.meow(c)

c.weight = 10
print(c.weight)