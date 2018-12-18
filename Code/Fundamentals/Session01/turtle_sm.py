from turtle import * 

speed (-1)
shape("turtle")
color("red")

for i in range(4):
    forward(100)
    left(90)

for i in range(50):
    right(20)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)

mainloop()