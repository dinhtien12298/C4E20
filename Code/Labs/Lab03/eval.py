# define
# argument
def calc(x, y, ope): 
    if ope == '+':
        res = x + y
    elif ope == '-':
        res = x - y
    elif ope == '*':
        res = x * y
    elif ope == '/':
        res = x / y
    
    return res

# call
# result = calc(3, 5, '+')
# print(result)