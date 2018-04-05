n = int(input('Enter a positive integer: '))
print('Yes') if n % 4 == 0 and n % 100 != 0 or n % 400 == 0 else print('No')
