vowels = ['a', 'e', 'i', 'o', 'u']
word = 'interstellar'
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

print(sorted(found))
