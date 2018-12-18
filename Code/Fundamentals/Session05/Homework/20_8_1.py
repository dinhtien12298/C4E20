strg = input("Enter a string: ").lower()

alphabet = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}

alphabet1 = {}
alphabet2 = {}
letter = list(strg)

for index,item in enumerate(letter):
    if item not in alphabet1:
        alphabet1[item] = 1
    elif item in alphabet1:
        alphabet1[item] += 1

for key, value in alphabet.items():
    if key in alphabet1:
        alphabet2[key] = alphabet1[key]

for key1, value1 in alphabet2.items():
    print(key1,value1)
