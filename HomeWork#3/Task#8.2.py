def enter_number():
    while True:
        number = input("Enter number: ")
        try:
            number = float(number)
        except ValueError:
            print('This is not number!')
        else:
            return number


r = enter_number()
print(r)
