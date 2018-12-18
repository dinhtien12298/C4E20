farm = {}
time = 4

for i in range (time+1):
    if i == 0:
        farm[i] = 1
    elif i == 1:
        farm[i] = 2
    else:
        farm[i] = farm[i-1] + farm[i-2]
for key, value in farm.items():
    print("MONTH", key, ":", value, "pair(s) of rabbit" )