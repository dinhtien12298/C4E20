from turtle import *

colors =['red', 'blue', 'brown', 'yellow', 'grey']

for i in range (5):
    begin_fill()
    fillcolor(colors[i])
    for j in range(2):
        forward(100)
        left(90)
        forward(200)
        left(90)
    forward(100)
    end_fill()


mainloop()