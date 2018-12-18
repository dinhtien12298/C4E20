word = ["hc","ng","pt","eny","any","ns","ngta","lm","r","stt"]

mean = {
    "hc": "học",
    "ng": "người",
    "pt": "personal trainer",
    "eny": "em người yêu",
    "any": "anh người yêu",
    "ns": "nói",
    "ngta": "người ta",
    "lm": "làm",
    "r": "rẻ rách",
    "stt": "status"
}

loop = True

while loop:
    for key in mean.keys():
        print(key, end="\t")
    print()
    code = input("Your code? ")
    print("* " * 50)
    if code in mean:
        print("Translation:", mean[code])
    else:
        code1 = input("Not found, do you want to contribute this word? (Y/N) ").upper()
        if code1 == "Y":
            value1 = input("Enter your translation: ")
            mean[code] = value1
            print("Updated")
        else:
            loop = False
    print("* " * 50)

