#слон бьет поле или нет?
x = int(input ('введите столбец начальной клетки '))
y = int(input ('введите строку начальной клетки '))
a = int(input ('введите столбец конечной клетки '))
b = int(input ('введите строку конечной клетки '))

if (a-x) == (b-y) or (a-x) == (y-b):
    print ('YES')
else:
    print ('NO')