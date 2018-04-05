a = float(input('Enter number a: '))
b = float(input('Enter number b: '))
c = float(input('Enter number c: '))

a, b, c = sorted([a, b, c])[0], sorted([a, b, c])[1], sorted([a, b, c])[2]

print('a = {}; b = {}; c = {}'.format(a, b, c))
