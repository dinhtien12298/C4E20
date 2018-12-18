# yeu cau 1
prices = {}

prices["banana"] = 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3

# yeu cau 2
stock = {}

stock["banana"] = 6
stock["apple"] = 0
stock["orange"] = 32
stock["pear"] = 15

# yeu cau 3
for key, value in prices.items():
    if key in stock:
        print("*", key)
        print("* price: ", value)
        print("* stock: ", stock[key])
    print()

# yeu cau 4
total = 0
for key1, value1 in stock.items():
    print(key1, ": $", value1 * prices[key1])
    total += value1 * prices[key1]
print()

print("You can earn total $", total)






