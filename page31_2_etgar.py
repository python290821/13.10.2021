# contributed by the class
a = int(input('enter 1st number: ')) 
b = int(input('enter 2nd number: ')) 
gap = (b - a) // abs(a - b)
for index in range(a, b + gap, gap):
    print(index)
