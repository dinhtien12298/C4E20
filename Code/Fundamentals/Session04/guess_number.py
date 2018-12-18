from random import randint

highest = 100
smallest = 1

print('''Guess your number Game
Now thinking about a number and press "Enter"''')
print('''Enter
"C" if my guess is correct
"S" if my guess is smaller than your number
"B" if my guess is bigger than your number''')
loop = True
while loop:
    r = (highest + smallest) // 2
    n = input("Is {} your number? ".format(r))
    if n == "C":
        print("I knew it")
        loop = False
    elif n == "S":
        smallest = r
    elif n == "B":
        highest = r




    

