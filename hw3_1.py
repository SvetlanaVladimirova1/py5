c1 = frozenset(("спальный мешок", "палатка", "фонарик", "одежда",))
c2 = frozenset(("продукты", "фонарик", "одежда", "посуда",))
c3 = frozenset(("фонарик", "одежда", "продукты",))

my_dict = {'Иван': c1, 'Петр': c2, 'Василий': c3, }
print(my_dict)

new_set = c1 | c2 | c3
print(f'{new_set = } Эти вещи взяли все три друга')

my_set1 = c1 - c2 - c3
print(f'{my_set1 = } Эти вещи уникальны')

my_set2 = c1 & c2 & c3
print(f'{my_set2 = } Эти вещи есть у каждого')

for k, v in my_dict.items():
        r = (c1 & c2 - c3)
        r1 = (c2 & c3 - c1)
        r2 = (c1 & c3 - c2)
print(f'{r = } Эти вещи есть у всех кроме Василия')
print(f'{r1 = } Эти вещи есть у всех кроме Ивана')
print(f'{r2 = } Эти вещи есть у всех кроме Петра')

my_dict.update(dict(Макар=c1))
print(my_dict)
