def check_query(query):
    tokens = query.split(',')
# напишите код тела функции
    query = str(q)
    query = q.split(', ')
    return query[1].strip(' ')


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
