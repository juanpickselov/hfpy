first = [1, 2, 3, 4, 5]
second = first
print(first)
print(second)
second.append(6)
print(first)
print(second)
print('Note how first and second are pointing to the same list!')
third = second.copy()
third.append(7)
print(third)
print(second)
print('Note how modifying third did not affect first or second')

