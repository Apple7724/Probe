# Разность двух множеств выводится на экран функцией print_valid_cities
# списком с разделением запятой
def print_valid_cities(a,b):
    c = a.difference(b)
    print(','.join(c))

# Пересечение двух множеств выводится на экран функцией print_common_cities
# списком с разделением запятой
def print_common_cities(a,b):
    c = a.intersection(b)
    print(','.join(c))

all_cities = set([
    'Абакан',
    'Астрахань',
    'Бобруйск',
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк',
    'Новосибирск'
])

used_cities = set(['Калуга', 'Абакан' , 'Новосибирск'])


print_valid_cities(all_cities, used_cities)

print_common_cities(all_cities, used_cities)

# объединение двух множеств

def print_shopping_list(recipe1, recipe2): 
    a = set(recipe1)
    b = set(recipe2)
    c = a.union(b)
    print(','.join(c))


pizza = ['мука', 'помидоры', 'шампиньоны', 'сыр', 'оливковое масло']
salad = ['огурцы', 'перцы', 'помидоры', 'оливковое масло', 'листья салата']

print_shopping_list(pizza, salad)
