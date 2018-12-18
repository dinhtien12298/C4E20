n = int(input("Input a number: "))
stt = True
k = 1
while stt:
    m = 10 ** k
    if (n-m) < 0:
        print("Your number have", k , "digits")
        stt = False
    else:
        k += 1
    

