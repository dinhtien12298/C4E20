n = int(input("Input a number please "))

for i in range(2*n):
    if i % 2 == 0:
        print("1", end=" ")
    else:
        print("0", end=" ")