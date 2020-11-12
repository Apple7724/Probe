# задаем декоратор:

def benchmark(func):
    
    # импортируем библиотеку time
    import time
    
    # создаем обертку:
    def wrapper():
        start = time.time()#вызов метода(функции)time() для расчета начала
        # действия программы
        
        func()# вызов функции(которая является аргументом декоратора
        
        end = time.time()#вызов метода(функции)time() для расчета конца
        # действия программы
        
        print(f'Время выполнения: {end-start} секунд.')
    return wrapper

# использование декоратора при вызове функции hello_world()
# нужно перед определением функции написать @benchmark

@benchmark
def format_string():
    weather = 'облачно'
    print('На улице сейчас {}.'.format(weather))
    
# запуск программы(функции)
format_string()

@benchmark
def f_string():
    weather = 'облачно'
    print(f'На улице сейчас {weather}.')
    
# запуск программы(функции)
f_string()








