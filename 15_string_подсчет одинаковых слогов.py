word = input('введите слово ')
number = len(word)
k = 0
n = 0
count = 0
for k in range (0, number):
        first = word[k:k+2]
        for n in range (k, number):
                second = word[n+1:n+3]
                print (k, 'first=',first)
                print (n, 'second=',second)
                if first == second:
                        count +=1
print ('одинаковых слогов здесь=',count)
        
    
