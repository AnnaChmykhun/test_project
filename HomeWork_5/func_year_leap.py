def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        result = True
    else:
        result = False
    return result