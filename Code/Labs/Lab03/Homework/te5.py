from turtle import *

def draw_star(x, y, length):
    penup()
    goto(x, y)
    pendown()
    left(108)
    for i in range(5):
        forward(length)
        left(144)
    mainloop()
