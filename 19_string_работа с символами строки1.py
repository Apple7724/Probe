s = input('введите любое слово ')
k = 0
while k < 5:
    k = k+1
    symbol = int (input('введите номер символа '))
    if symbol > len(s):
        print ('введите номер символа не более ',len(s))
    else:
        otvet = s[symbol-1]
        print (otvet)

