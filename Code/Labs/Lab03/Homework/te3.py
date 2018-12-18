from turtle import *

def draw_square(length, colour):
    color(colour)
    for i in range(4):
        forward(length)
        left(90)
        mainloop()
