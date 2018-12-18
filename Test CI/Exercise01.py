number_input = input("Nhập vào 1 dãy số, cách nhau bởi dấu ' ': ")

number_raw = list(number_input)
number_final = []

number_of_space = 0

for index, item in enumerate(number_raw):
    if item == ' ':
        number_of_space += 1

loop = True
count = 0
n = -1
while loop:
    for index, item in enumerate(number_raw):
        if item == ' ':
            number = [int("".join(number_raw[n+1:index]))]
            number_final.append(number[0])
            del number
            n = index
            count += 1
    if count == number_of_space:
        number = [int("".join(number_raw[n+1:len(number_raw)]))]
        number_final.append(number[0])
        break
            
print("Dãy số vừa nhập:")
for index1, item1 in enumerate(number_final):
    print(item1)
