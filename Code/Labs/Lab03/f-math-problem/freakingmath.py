from random import *
from eval import calc

def generate_quiz():
    x = randint(1, 10)
    y = randint(1, 10)

    op = ['+', '-', '*', '/']
    ope = choice(op)

    res = calc(x, y, ope)

    error = randint(-1, 1)
    r = res + error
    
    return [x, y, ope, r]

def check_answer(x, y, op, result, user_choice):
    x = randint(1, 10)
    y = randint(1, 10)

    op = ['+', '-', '*', '/']
    ope = choice(op)

    res = calc(x, y, ope)

    if r == res:
        user_choice = True
    elif r != res:
        user_choice = False

    return [x, y, ope, r, user_choice]
