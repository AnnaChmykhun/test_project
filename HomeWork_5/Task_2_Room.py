class Room:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area_of_room(self):
        return self.side_a * self.side_b

    def perimeter_of_room(self):
        return (self.side_a + self.side_b) * 2


if __name__ == '__main__':
    r1 = Room(5, 10)
    print(r1.area_of_room())
    print(r1.perimeter_of_room())
