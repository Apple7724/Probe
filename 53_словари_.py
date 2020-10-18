friends =  {'Серёга': 'Омск',
            'Соня': 'Москва',
            'Дима': 'Челябинск',
            'Вася': 'Питер',
            'Петя': 'Красноярск'}

print('Вот в каких городах живут мои друзья:')
print(', '.join(friends.values()))

print('Вот в каких городах живут мои друзья:',', '.join(friends.values()))

for i in friends:
    print(i + ' живет в городе ' + friends[i])

for i, j in friends.items():
    print(i + ' живет в городе ' + j)
