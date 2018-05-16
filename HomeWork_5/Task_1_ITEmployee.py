from Task_1_Employee import Employee


class ITEmployee(Employee):
    def __init__(self, *args):
        super().__init__(*args)
        self.skills = []

    def add_skill(self, new_skill):
        self.skills.append(new_skill)

    def add_skills(self, *args):
        self.skills.extend(args)


if __name__ == "__main__":
    ite1 = ITEmployee('Anna Ch', 1992, 'QA Engineer', 2, 100)
    ite1.add_skill('Test Plans')
    print(ite1.skills)
    ite1.add_skills('Test Cases', 'Linux', 'Python')
    print(ite1.skills)
