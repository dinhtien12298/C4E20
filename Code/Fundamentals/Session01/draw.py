from turtle import * 

n = int(input("Nhap so canh cua da giac "))

speed (+1)
shape("turtle")
color("red")

for i in range(n):
    forward(100)
    left(180-180*(n-2)/n)

# for i in range(n):
#     forward(100)
#     left(360/n)

mainloop()