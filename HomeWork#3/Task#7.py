def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            result = 'Equilateral triangle'
        elif a == b or b == c or a == c:
            result = 'Isosceles triangle'
        else:
            result = 'Versatile triangle'
    else:
        result = 'Not a triangle'
    return result


a1 = float(input('Enter positive number a: '))
b1 = float(input('Enter positive number b: '))
c1 = float(input('Enter positive number c: '))

r = triangle(a1, b1, c1)
print(r)
