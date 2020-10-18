a=5
for i in range(1,66):
    a= a*3-1
    print ('шаг= ',i)
    print(a)
    b=str(a)
    a=int(b[-1])
    print('остаток= ',a)

