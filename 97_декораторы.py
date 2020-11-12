# задаем декоратор:
def decorator_function(func):
    
    # создаем обертку:
    
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()# вызов функции(которая является аргументом декоратора
        print('Выходим из обёртки')
        print()
    return wrapper

# использование декоратора при вызове функции hello_world()
# нужно перед определением функции написать @decorator_function:

@decorator_function
def hello_world():
    print('Hello world!')

# запуск программы(функции):

hello_world()
# аналогично:
decorator_function(hello_world())

# ещё пример:

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        print()
        return modified_result
    return wrapper

@uppercase
def text_func():
    return 'Hello Bob!'
    

print(text_func())





