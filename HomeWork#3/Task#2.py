s = input('Enter a string: ')

print(s[len(s)//2:]+s[:len(s)//2]) if len(s) % 2 == 0 else print(s[len(s)//2 + 1:]+s[:len(s)//2 + 1])
