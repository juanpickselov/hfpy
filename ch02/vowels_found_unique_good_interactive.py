vowels = ['a', 'e', 'i', 'o', 'u']
word = input('word to use:')
found = []
for letter in word:
    if letter.lower() in vowels:
        if letter not in found:
            found.append(letter.lower())

print(sorted(found))
