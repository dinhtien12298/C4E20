# đưa tất cả kí tự về lower
name1 = input("Your full name: ").lower()
char = list(name1)

# biến kí tự đầu tiên thành viết hoa
char[0] = char[0].upper()

# xóa các khoảng trắng liền nhau và viết hoa chữ đầu
for index, item in enumerate(char):
    while item == " ":
        char[index+1] = char[index+1].upper()
        if char[index+1] == " ":
            del char[index+1]
        else:
            break

# merge các element của list vào với nhau
name2 = ["".join(char[0:len(char)])]

# hiển thị tên sau khi sửa
print("Updated:", *name2)