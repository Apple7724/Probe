a = int(input ("введите трехзначное число "))
b = int(a//100)
c = int(a/10 - 10*b)
d = int(a - 100 * b - 10 * c)
if (a > 99 and a < 1000):
    print ('здесь ', b, " сотен")
    print ('здесь ', c, " десятков")
    print ('здесь ', d, " единиц")
    print ('произведение цифр этого числа ', b * c * d)
else:
    print ('это не трехзначное число')
