a = int(input('Enter an integer a: '))
b = int(input('Enter an integer b: '))
c = int(input('Enter an integer c: '))

if a == b == c:
    print('3')
elif a == b != c or a == c != b or b == c != a:
    print('2')
else:
    print('0')

