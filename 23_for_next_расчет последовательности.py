first = int(input('введите первый член последовательности '))
last = int(input('введите последний член последовательности '))
k = 0
summ = 0
for i in range (first , last+1):
        summ = summ + i
        k +=1
print (' сумма = ',summ)
print (' число членов последовательности = ',k)       
print (' среднее арифметическое = ',summ/k) 
        
        

