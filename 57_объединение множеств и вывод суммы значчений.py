# напишите здесь функцию print_shopping_list(),
# подобрав уникальные названия продуктов и сложив значения
def print_shopping_list(dish1, dish2):
    dish1 = set(pizza.keys())
    dish2 = set(salad.keys())
    dishes = dish1.union(dish2)
    for i in dishes:
        if i in dish1:
            if i in dish2:
                a = float(pizza[i])+float(salad[i])
                print(i, ':', a)
            else:
                print(i, ':', pizza[i])
        else:
                print(i, ':', salad[i])
        

pizza = {'мука, кг': 1,
         'помидоры, кг': 1.7,
         'шампиньоны, кг': 1.5,
         'сыр, кг': 0.8,
         'оливковое масло, л': 0.1,
         'дрожжи, г': 50}
salad = {'огурцы, кг': 1,
         'перцы, кг': 1,
         'помидоры, кг': 1.5,
         'оливковое масло, л': 0.3,
         'листья салата, кг': 0.4}

print_shopping_list(pizza, salad)

# более правильное решение: моя ошибка в коде в том, что наличие элемента
# в dish2 проверяется только при верности факта наличия в dish1
def print_shopping_list(dish1,dish2):
    
    dish=set(dish1)
    
    dish = dish.union(dish2)
    
    for i in dish:
        weight=0;
        if i in dish1.keys():
            weight+=dish1[i]
        if i in dish2.keys():
            weight+=dish2[i]    
        print (i+':', weight)


print_shopping_list(pizza, salad)
