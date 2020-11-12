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
def hello_world():
    print('Hello world!')
    
# запуск программы(функции)
hello_world()

# аналогично:
benchmark(hello_world())





