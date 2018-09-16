vowels = ['a', 'e', 'i', 'o', 'u']
word = 'interstellar'
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
    # Note while the indentation looks good
    # we're getting duplicate letters printed
    # when we wanted a unique list of vowels
    # should be a suite far left
    for vowel in found:
        print(vowel)
