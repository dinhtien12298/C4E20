from random import choice

words = ["champion","dungeon","vodka"]
word = choice(words)

chars = list(word)
updated_chars = []

loop = True

while loop:
    rand_char = choice(chars)
    updated_chars.append(rand_char)
    chars.remove(rand_char)
    if len(chars) == 0:
        loop = False

print(*updated_chars)

ans = input("Your guess: ")
if ans == word:
    print("Huraaaa")
else:
    print(":<")
        

