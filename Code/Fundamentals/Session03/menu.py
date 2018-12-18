# list
menu = ["Rice", "Fish", "Beef"]

# Separator
# print(*menu,sep=", ")

# length
# print(len(menu))

# menu.append("Egg")
# print(len(menu))

# for i in range(len(menu)):
#     print(menu[i])

for index, item in enumerate(menu):
    print(index + 1, item, sep=". ")

# for item in menu:
#     print(item)

# for index, item in enumerate(menu):
#     print("{}. {}".format(index + 1, item))

# update
# print(*menu, sep=", ")
# menu[2] = "Candy"
# print(*menu, sep=", ")