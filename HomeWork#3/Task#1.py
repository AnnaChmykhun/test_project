while True:
    s = input('Enter a string: ')
    try:
        s[2]
    except IndexError:
        print('Entered string is too short. At least six symbols required.')
    else:
        print(s[2], s[-2], s[:5], s[:-2], s[::2], s[1::2], s[::-1], s[::-2], s[-2:0:-1], len(s), sep='\n')
        break
