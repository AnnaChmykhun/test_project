def value(*numbers):
    s = list(numbers)
    s.sort()
    for i in range(0, len(s)):
        if s[i] == s[i+1]:
            continue
        else:
            return s[i+1]


print(value(8, 4, 1, 10, 1, 1, 1, 6, 89))
