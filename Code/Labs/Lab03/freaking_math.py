from random import randint, choice
from eval import calc

cal = True
score = 0
while cal:
    x = randint(1, 10)
    y = randint(1, 10)

    op = ['+', '-', '*', '/']
    ope = choice(op)

    res = calc(x, y, ope)

    error = randint(-1, 1)
    r = res + error

    print('* ' * 10)
    print('{} {} {} = {}'.format(x, ope, y, r))
    print('* ' * 10)
    ans = input('(Y/N)? ').upper()

    if ans == 'Y':
        if r == res:
            print('Right!')
            score += 1
        elif r != res:
            print('Wrong!')
            cal = False
    elif ans == 'N':
        if r == res:
            print('Wrong!')
            cal = False
        elif r != res:
            print('Right!')
            score += 1
    else:
        calc = False

    print('Your Score Is:', score)