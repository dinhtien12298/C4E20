b = int(input("How many B bacterias are there? "))
time = int(input("How much time in minutes will we wait? "))

b_time = int(b * 2 * (time/2))

print("After", time, "minutes, we will have", b_time, "bacterias")