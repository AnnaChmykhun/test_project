from Task_1_Person import Person


class Employee(Person):
    def __init__(self, full_name, year_of_birth, position, experience, salary):
        super().__init__(full_name, year_of_birth)
        self.position = position
        self.experience = experience
        self.salary = salary

    def detailed_position(self):
        if self.experience < 3:
            self.position = 'Junior' + ' ' + self.position
        elif 3 <= self.experience <= 6:
            self.position = 'Middle' + ' ' + self.position
        elif self.experience > 6:
            self.position = 'Senior' + ' ' + self.position
        return self.position

    def update_salary(self, increment):
        self.salary += increment
        return self.salary


if __name__ == "__main__":
    e1 = Employee('Anna Ch', 1992, 'QA Engineer', 2, 100)
    print(e1.detailed_position())
    print(e1.update_salary(100))
