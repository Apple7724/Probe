def func(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

func('hello')
print()
func('hello', 1, 2, 3)
print()
func('hello', 1, 2, 3, key1='haha',key2='hoho')

