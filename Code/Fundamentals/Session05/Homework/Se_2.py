list1 = [1, 2, 0, 2, 1, 9, 9 ,8, 1, 7, 0 ,9, 1, 9, 9, 6]
numb = int(input("Enter a number: "))

numbers = {}

for index, item in enumerate(list1):
    if item not in numbers:
        numbers[item] = 1
    elif item in numbers:
        numbers[item] += 1

print(numb, "appears",numbers[numb] ,"times in my list")




