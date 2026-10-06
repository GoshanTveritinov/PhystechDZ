from random import randint
from tkinter import *



class Ball:
    def __init__(self, *args, color = 'green'):
        self.R = randint(20, 60) #храним размер, при каждом создании объекта будет выбираться случайно
        self.x = randint(self.R, root.winfo_width() - self.R) # храним положение по x и y
        self.y = randint(self.R, root.winfo_height() - self.R)
        self.dx, self.dy = (10, 10) # это по сути шаг движения шаров. если увеличить -- будут двигаться быстрее
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill=color) # при создании шарика отрисовываем его

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > root.winfo_width() or self.x - self.R <= 0: # отражение от стенок
            self.dx = -self.dx
        if self.y + self.R > root.winfo_height() or self.y - self.R <= 0: # отр
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


#здесь мы уже привычно обращаемся к balls как к глобальной переменной. На самом деле дело в том, что нам лень писать классы.
def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


root = Tk()
root.geometry("500x500")
root.update()

canvas = Canvas(root)
canvas.pack(fill = BOTH, expand = TRUE)


num = 10

new_ball = lambda *args: balls.append(Ball(color = f"#{randint(0, 0xFFFFFF):06x}"))


canvas.bind('<Button-1>', new_ball)


balls = [Ball() for i in range(num)]



# делаем шаг перемещения и отрисовки шаров. поскольку mainloop циклит наше приложение, это будет происходить, пока мы не закроем окно
tick()
root.mainloop()