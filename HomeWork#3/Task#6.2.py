def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


a1 = float(input('Enter positive number a: '))
b1 = float(input('Enter positive number b: '))
c1 = float(input('Enter positive number c: '))

r = is_triangle(a1, b1, c1)
print(r)


