balance1 = input("Enter your balance: ")

list1 = list(balance1)

# xóa số 0 ở đầu nếu có và các kí tự linh tinh như "." "," " " để sắp xếp lại toàn bộ
for index, item in enumerate(list1):
    while list1[0] == "0":
        if list1[index+1] == "0":
            del list1[0]
            del list1[index+1]
        else:
            del list1[0]
            break
    if item == " ":
        del list1[index]
    elif item == ",":
        del list1[index]
    elif item == ".":
        del list1[index]

# tạo list riêng chỉ chứa "," và thêm dần vào các list1 được chia thành từng bộ 3 số một
n = len(list1) % 3
number = ["$"]
if n != 0:
    number += list1[0: n]
for i in range (n,len(list1)+1,3):
    list2 = [","]
    list2 += list1[i: i+3]
    number += list2

# thuật toán trên làm cho xuất hiện "," ở đầu hoặc cuối dãy số trong 1 số trường hợp nên ta xóa bỏ chúng
for index1, item1 in enumerate(number):
    if number[1] == ",":
        del number[1]
    if number[len(number)-1] == ",":
        del number[len(number)-1]

# merge các element của list vào với nhau
balance2 = ["".join(number[0:len(number)])]

# hiển thị số dư sau khi sửa
print("Your updated balance:", *balance2)