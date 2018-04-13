def enter_word():
    while True:
        word = input('Enter word: ').strip()
        if ' ' not in word:
            result = word
            break
    return result


r = enter_word()
print(r)
