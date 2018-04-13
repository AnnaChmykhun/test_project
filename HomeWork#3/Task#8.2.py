def enter_number():
    while True:
        number = input("Enter number: ")
        try:
            number = float(number)
        except ValueError:
            pass
        else:
            result = number
            break
    return result


r = enter_number()
print(r)
