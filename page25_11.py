
x = int(input('please enter a number'))
digits = 1
x = x // 10
while x > 0:
    digits += 1
    x = x // 10

print(f'number of digits: {digits}')
