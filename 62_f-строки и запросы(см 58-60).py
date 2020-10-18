DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count_string = format_count_friends(len(DATABASE))
        return f'У тебя {count_string}'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE.keys())
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'

def process_friend(name, query):
    if name in DATABASE:
        #tokens = query.split(', ')
        #query = tokens[1]
        if query == 'ты где?':
            city = DATABASE[name]
            return f'{name} в городе {city}'
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'
    
def process_query(query):
    tokens = query.split(', ')
    name = tokens[0]
    query = tokens[1]
    if name == 'Анфиса':
        return process_anfisa(query)
    else:
        return process_friend(name, query)

def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?'
    ]
    for query in queries:
        print(query, '-', process_query(query))


runner()
