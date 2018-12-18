sheep_sz = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Tien and there are my sheeps sizes:")
print(sheep_sz)

highest = max(sheep_sz)
print("Now my biggest sheep has size:", highest,". Let's shear it!")

for index, item in enumerate(sheep_sz):
    if item == highest:
        sheep_sz[index] = 8
        print("After shearing, here is my flock:")
        print(sheep_sz)
