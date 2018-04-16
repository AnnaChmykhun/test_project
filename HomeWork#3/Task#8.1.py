def enter_word():
    while True:
        word = input('Enter word: ').strip()
        if ' ' not in word:
            return word


r = enter_word()
print(r)
