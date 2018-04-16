def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return 'Equilateral triangle'
        elif a == b or b == c or a == c:
            return 'Isosceles triangle'
        else:
            return 'Versatile triangle'
    else:
        return 'Not a triangle'


a1 = float(input('Enter positive number a: '))
b1 = float(input('Enter positive number b: '))
c1 = float(input('Enter positive number c: '))

r = triangle(a1, b1, c1)
print(r)
