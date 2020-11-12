def func(*a):
    for i in a:
        print(i)
        print()

func(2,12,85,'06')

def func_kwargs(**b):
    for i,k in b.items():
        print(k)
        print()

func_kwargs(c=2,d=12,e=85,f='06')

def func2(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)
print('вывод обязательного агрумента')
func2('hello')
print('вывод кортежа из необязательных аргументов (*args)')
func2( 'hello', 1, 2, 3)
print('вывод словаря из необязательных аргументов  (*kwargs)')
func2('hello', key1='haha',key2='hoho')
print('все вместе:')
func2('hello', 1, 2, 3, key1='haha',key2='hoho')
