data = input("Введите строку:  ")
print(data)
new_text = data.replace(',', ''). \
        replace('.', ''). \
        replace(' ', ''). \
        replace('!', ''). \
        replace('?', ''). \
        replace('"', ''). \
        lower()
dict1 = {}
for item in new_text:
    counter = new_text.count(item)
    dict1[item] = counter
print(dict1)
