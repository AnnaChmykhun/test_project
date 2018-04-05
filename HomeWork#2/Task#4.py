a = float(input('Enter positive number a: '))
b = float(input('Enter positive number b: '))
c = float(input('Enter positive number c: '))

print('Yes') if a + b > c and a + c > b and b + c > a else print('No')
