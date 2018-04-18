def song(number_of_rows=3, number_of_la=3, sign=0):
    s = ''
    for i in range(number_of_la):
        s += 'la-'
    s = s.rstrip('-')

    r = ''
    for j in range(number_of_rows):
        r += '\n' + s
    r = r.lstrip('\n')

    if sign == 0:
        r = r + '.'
    elif sign == 1:
        r = r + '!'

    return r


print(song(2, 7, 1))
