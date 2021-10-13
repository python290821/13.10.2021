
x = int(input('please enter a number'))
opposite = 0

while x > 0:
    opposite = opposite * 10 + (x % 10)
    x = x // 10

print(f'opposite is: {opposite}')
