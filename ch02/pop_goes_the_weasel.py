my_list = ['pop', 'goes', 'the', 'weasel']
first_list = ['on', 'a']
second_list = ['clear', 'day']
first_list.extend(second_list)
print(my_list)
my_list.pop()
print(my_list)
print(first_list)
first_list.insert(0,'forever')
first_list.insert(0,'see')
first_list.insert(0,'can')
first_list.insert(0,'you')

print(first_list)
