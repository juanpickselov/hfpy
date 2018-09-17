phrase = "Don't panic!"
phrase_list = list(phrase)
print(phrase)
print(phrase_list)

for num in range(4):
    phrase_list.pop()
phrase_list.pop(0)
phrase_list.remove("'")
phrase_list.extend([phrase_list.pop(), phrase_list.pop()])
phrase_list.insert(2, phrase_list.pop(3))
new_phrase = ''.join(phrase_list)
print(phrase_list)
print(new_phrase)
