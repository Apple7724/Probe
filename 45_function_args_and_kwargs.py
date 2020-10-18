def func(*a):
    for i in a:
        print(i)

func(2,12,85,'06')

def func_kwargs(**b):
    for i,k in b.items():
        print(k)

func_kwargs(c=2,d=12,e=85,f='06')
