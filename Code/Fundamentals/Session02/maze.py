from turtle import *

speed(-1)
shape("turtle")
color("red")

for i in range(0, 800, 10):
    forward(i)
    left(90)

mainloop()