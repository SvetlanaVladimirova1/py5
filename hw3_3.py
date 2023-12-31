text = "Пушкин чувствует необходимость житейских перемен. " \
        "В 1830 году повторное его сватовство к Наталье Николаевне Гончаровой было принято, " \
        "и осенью поэт отправляется в Болдино, нижегородское имение отца, чтобы вступить во владение " \
        "близлежащей деревней Кистенёво, подаренной отцом к свадьбе. Холерные карантины задержали поэта " \
        "на три месяца, и этой поре было суждено стать знаменитой Болдинской осенью, наивысшей точкой" \
        " пушкинского творчества, когда из-под его пера вылилась целая библиотека " \
        "произведений: «Повести покойного Ивана Петровича Белкина» («Повести Белкина»), " \
        "«Опыт драматических изучений» («Маленькие трагедии»), последние главы «Евгения Онегина», " \
        "«Домик в Коломне», «История села Горюхина», «Сказка о попе и о работнике его Балде»," \
        "несколько набросков критических статей и около тридцати стихотворений."
new_text = text.replace(',', ''). \
        replace('.', ''). \
        replace('!', ''). \
        replace('?', ''). \
        replace('"', ''). \
        lower()
dict1 = {}
dict2 = {}
words = new_text.split()
print(words)
for item in words:
    counter = words.count(item)
    dict1[item] = counter
    new_dict1 = sorted(dict1.values())[::-1]
print(new_dict1)
for i in new_dict1:
    for j in dict1.keys():
            if dict1[j] == i:
                dict2[j] = dict1[j]
print(list(dict2.items())[:10])
