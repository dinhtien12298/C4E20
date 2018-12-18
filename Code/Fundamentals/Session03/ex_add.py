menutoday = ["Rice", "Fish", "Beef"]
print("Here is your menu today")
print(*menutoday,sep=", ")
food = input("Add a food U want ")
menutoday.append(food)
print(*menutoday,sep=", ")