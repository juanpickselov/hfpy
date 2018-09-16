words = ['Bonjour', 'tout', 'le', 'monde']
mixed_stuff = ['apple', 1, 42.0, True]
list_of_Lists = [words, mixed_stuff]


for item in mixed_stuff:
    print(type(item))

print()

for item in  list_of_Lists:
    print(type(item))
