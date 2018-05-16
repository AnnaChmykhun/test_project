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
