user_query = 'как стать бэкенд-разработчиком'

url = 'https://yandex.ru/search/?text=' # ваш код здесь
first_list = user_query.split(' ')
transformed = '%20'.join(first_list)
print(url+transformed)

# в одну строку пробуем тоже:

user_query = 'как стать бэкенд-разработчиком'

url = 'https://yandex.ru/search/?text='+'%20'.join(user_query.split(' ')) # ваш код здесь
print(url)
