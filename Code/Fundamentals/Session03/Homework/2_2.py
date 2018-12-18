sheep_sz = [5, 7, 300, 90, 24, 50, 75]
biggest = 0

for sz in sheep_sz:
    if sz > biggest:
        biggest = sz

print('Now my biggest sheep has size', biggest, "let's shear it")