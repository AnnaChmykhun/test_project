def distance(x1, y1, x2, y2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return d


x_1 = float(input('Enter coordinate x1: '))
y_1 = float(input('Enter coordinate y1: '))
x_2 = float(input('Enter coordinate x2: '))
y_2 = float(input('Enter coordinate y2: '))

r = distance(x_1, y_1, x_2, y_2)
print(r)
