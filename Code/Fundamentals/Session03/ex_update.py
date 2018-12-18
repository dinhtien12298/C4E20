menutoday = ["Rice", "Fish", "Beef"]
print("Here is your menu today")
for index, item in enumerate(menutoday):
    print("{}. {}".format(index + 1, item))
number = int(input("Position U want to update? ")) - 1
food = input("Input a food U want to update ")
menutoday[number] = food
for index, item in enumerate(menutoday):
    print("{}. {}".format(index + 1, item))