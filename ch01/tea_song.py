word = 'bottles'
for tea_num in range(99, 0, -1):
    print(tea_num, word, 'of tea on the wall.')
    print(tea_num, word, 'of tea.')
    print('Take one down.\nPass it around.')
    if tea_num == 1:
        print('No more bottles of tea on the wall.')
    else:
        new_num = tea_num - 1
        if new_num == 1:
            word = 'bottle'
        print(new_num, word, 'of tea on the wall.')
    print()
