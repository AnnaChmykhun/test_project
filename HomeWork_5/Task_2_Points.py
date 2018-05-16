class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_to_point(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


if __name__ == '__main__':
    p1 = Point(6, 8)
    p2 = Point(6, 8)
    print(p1.distance_to_origin())
    print(p2.distance_to_origin())
    print(p1.distance_to_point(p2))
