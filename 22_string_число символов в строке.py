name = input('введите свое имя ')
surname = input('введите свою фамилию ')
print (len (name+surname))
print ('привет, ',name,' ',surname,' !')
c = (len (name+surname))%2
if c == 0:
    print (' здесь четное число символов')
else:
    print (' здесь нечетное число символов')
