# Nhập dãy số
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

# Tính toán
numb = []
for index,item in enumerate(number_final):
    n = 128 / item
    for index1, item1 in enumerate(number_final):
        if item1 == n and index != index1 and {'x':item,'y':item1,'z':index,'t':index1} not in numb and {'x':item1,'y':item,'z':index1,'t':index} not in numb:
            numb.append({'x':item,'y':item1,'z':index,'t':index1})

if len(numb) > 0:
    print("Có những cặp số sau có tích bằng 128")
    for index2,item2 in enumerate(numb):
        print("{} và {} ở vị trí {} và {}".format(item2['x'], item2['y'], item2['z'], item2['t']))
else:
    print("Không có cặp số nào có tích bằng 128")