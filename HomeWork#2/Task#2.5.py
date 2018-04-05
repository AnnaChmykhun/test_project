n = input('Enter positive float number: ')
L = len(n)
index_dot = n.index('.')
fraction = ''
for i in range(index_dot + 1, L):
    fraction += n[i]
print('Fraction of entered number is 0.{}'.format(fraction))
