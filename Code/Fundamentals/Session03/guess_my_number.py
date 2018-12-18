from random import randint

r = randint(1, 100)
count = 0
stt = True

while stt:
    n = int(input("Guess a number: "))
    if n < r:
        print("Too small :<")
    elif n > r:
        print("Too big :))")
    else:
        print("Bingo")
        stt = False
    count += 1
    if count == 7:
        stt = False
        if n != r:
            print("You lose idiot!!!")


        