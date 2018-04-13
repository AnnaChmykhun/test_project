def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        result = True
    else:
        result = False
    return result


a1 = float(input('Enter positive number a: '))
b1 = float(input('Enter positive number b: '))
c1 = float(input('Enter positive number c: '))

r = is_triangle(a1, b1, c1)
print(r)


