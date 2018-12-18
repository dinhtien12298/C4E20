x = int(input('x = '))
ope = input('Operation(+,-,*,/): ')
y = int(input('y = '))

res = 0
if ope == '+':
    res = x + y
elif ope == '-':
    res = x - y
elif ope == '*':
    res = x * y
elif ope == '/':
    res = x / y

print('* ' * 10)
print('{} {} {} = {}'.format(x, ope, y, res))
print('* ' * 10)