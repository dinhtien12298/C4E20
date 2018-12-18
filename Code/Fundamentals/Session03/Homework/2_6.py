sheep_sz = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Tien and there are my sheeps sizes:")
print(sheep_sz)

print()
highest = max(sheep_sz)
print("Now my biggest sheep has size:", highest,". Let's shear it!")
for index, item in enumerate(sheep_sz):
    if item == highest:
        sheep_sz[index] = 8
        print("After shearing, here is my flock:")
        print(sheep_sz)
print()

n = 4
for i in range (n-1):
    print("MONTH", i+1, ":")
    if i <2:
        for index2 in range (len(sheep_sz)):
            sheep_sz[index2] += 50
        print("One month has passed, now here is my flock:")
        print(sheep_sz)

        highest = max(sheep_sz)
        print("Now my biggest sheep has size:", highest,". Let's shear it!")

        for index, item in enumerate(sheep_sz):
            if item == highest:
                sheep_sz[index] = 8
                print("After shearing, here is my flock:")
                print(sheep_sz)
    else:
        for index2 in range (len(sheep_sz)):
            sheep_sz[index2] += 50
        print("One month has passed, now here is my flock:")
        print(sheep_sz)
        
        size_sum = 0
        for j in range (len(sheep_sz)):
            size_sum += sheep_sz[j]
        print("My flock has size in total:", size_sum)
        print("I would get",size_sum,"* $2 =","$",size_sum*2)
        
    print()