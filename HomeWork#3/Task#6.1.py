def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


r = is_year_leap(int(input('Enter a year: ')))
print(r)
