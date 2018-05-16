class Person:
    def __init__(self, full_name, year_of_birth):
        if len(full_name.split()) != 2:
            raise NameError("Invalid name!")
        else:
            self.full_name = full_name

        if year_of_birth < 1900 or year_of_birth > 2018:
            raise ValueError("Invalid year!")
        else:
            self.year_of_birth = year_of_birth

    def select_name(self):
        return self.full_name.split()[0]

    def select_surname(self):
        return self.full_name.split()[1]

    def age(self, years=2018):
        return years - self.year_of_birth


if __name__ == "__main__":
    p1 = Person('Anna Ch', 1992)
    print(p1.select_name())
    print(p1.select_surname())
    print(p1.age())
    print(p1.age(2078))
