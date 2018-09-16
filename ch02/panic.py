phrase = "Don't panic"
phrase_list = list(phrase)
print(phrase)
print(phrase_list)

new_phrase = ''.join(phrase_list)
print(phrase_list)
print(new_phrase)

# print(phrase_list)

phrase_list.pop(0)
phrase_list.pop(2)
phrase_list.pop(3)
phrase_list.insert(3, 'a')
phrase_list.insert(2, ' ')
for num in range(4):
    phrase_list.pop()
final_phrase = ''.join(phrase_list)
print(final_phrase)
