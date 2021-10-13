
a = int(input('enter 1st number: ')) # 5
b = int(input('enter 2nd number: ')) # 10
if a > b:
    gap = -1
else:
    gap = 1
for index in range(a, b + gap, gap):
    print(index)
