# Method#2
import decimal

n2 = decimal.Decimal(input('Enter positive float number: '))
fraction = n2 - int(n2)
print('Fraction of entered number is {}'.format(fraction))


# Method#1
# n1 = input('Enter positive float number: ')
# L = len(n1)
# index_dot = n1.index('.')
# fraction = ''
# for i in range(index_dot + 1, L):
#    fraction += n1[i]
# print('Fraction of entered number is 0.{}'.format(fraction))
