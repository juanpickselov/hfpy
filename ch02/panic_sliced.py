phrase = "Don't panic!"
phrase_list = list(phrase)
print(phrase)
print(phrase_list)

new_phrase = ''.join(phrase_list[1:3])
new_phrase = new_phrase + ''.join([phrase_list[5], phrase_list[4], phrase_list[7], phrase_list[6]])

print(phrase_list)
print(new_phrase)
