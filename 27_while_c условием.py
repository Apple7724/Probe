number = int(input ('введите число квадратов '))
n = int(input ('input n '))
i = 1
while i <= number:
    k = i**2
    if k <= n:
        print (k)
    else:
        print ('число ', k, 'превышает ',n)
    
    i +=1
    
