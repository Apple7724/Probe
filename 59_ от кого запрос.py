def check_query(query):
# напишите код тела функции
    if 'Анфиса' in q:
        return 'запрос к Анфисе'
    else:
        return 'запрос к кому-то еще'


# дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

for q in queries:
    result = check_query(q)
    print(q, '-', result)

# альтернативный код

def check_query(query):
# напишите код тела функции
    query = str(q)
    query = q.split(', ')
    if query[0] == 'Анфиса':
        return 'запрос к Анфисе'
    else:
        return 'запрос к кому-то еще'

for q in queries:
    result = check_query(q)
    print(q, '-', result)
