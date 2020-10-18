friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

#friends = {}

# перевод списков в словарь через кортежи (friends_names, friends_cities)
friends = {key: value for key, value in zip(friends_names, friends_cities)}

print("Лена живёт в городе " + friends['Лена'])

