from turtle import *

color("blue")
speed(-1)

left(120)

for i in range(40):
    for j in range(4):
        forward(160-4*i)
        left(90)
    right(10)

mainloop()