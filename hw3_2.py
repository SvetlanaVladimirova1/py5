my_list = [4, 8, 2, 3, 5, 6, 1, 3, 4, 9, 1, 7, 9, 5, 9, 2]
print(my_list)
my_list.sort()
print(my_list)
my_list2 = []
my_list1 = []
for item in my_list:
    c = my_list.count(item)
    if c > 1:
        my_list1.append(item)
for item in my_list1:
    if item not in my_list2:
        my_list2.append(item)
print(my_list2)
