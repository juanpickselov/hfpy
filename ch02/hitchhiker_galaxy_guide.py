book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print(booklist)
article = booklist[0:3]
print(''.join(article), ''.join(booklist[-6:]))

reverse_title = ''.join(booklist[::-1])
print(reverse_title)
print(booklist)

every_other = ''.join(booklist[::2])
print(every_other)
hitchhiker = ''.join(booklist[4:14])
rekihhctih = ''.join(booklist[13:3:-1])

print(hitchhiker)
print(rekihhctih)

