n = int(input("Enter range of sides (n>1) "))

s = n // 5 + 1
for i1 in range(4):
    if i1 == 2:
        s += 1
    for i11 in range(n):
        print("* ", end="")
    for i12 in range(s):
        print("  ", end="")
print()
s = n // 5 + 1

for i2 in range(n - 1):
    print("* ", end="")
    for i21 in range (n - 1 + s):
        print("  ", end="")
    print("* ", end="")
    for i22 in range (n - 2):
        print("  ", end="")
    print("* ", end="")
    for i23 in range(s):
        print("  ", end="")
    print("* ", end="")
    for i24 in range(n - 1):
        print("  ", end="")
    print("* ", end="")
    for i25 in range(s):
        print("  ", end="")
    if i2 == (n-2)//2:
        for i26 in range(n):
            print("* ", end="")
        print()
    else:
        print("* ")

for i3 in range(4):
    if i3 == 2:
        s += 1
    for i31 in range(n):
        print("* ", end="")
    for i32 in range(s):
        print("  ", end="")


