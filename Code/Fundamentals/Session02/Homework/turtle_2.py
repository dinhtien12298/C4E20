from turtle import * 

n = 3

color("red")

for i in range(4):
    if n % 2 == 1:
        color("blue")
    else:
        color("red")
    for j in range(n):
        forward(100)
        left(360/n)
    n += 1

mainloop()