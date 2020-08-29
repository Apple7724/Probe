word = input('введите предложение ')
number = len(word)
count = 1
for k in range (0, number):
        if word[k] == ' ':
                        count +=1
print ('число слов здесь=',count)
        
    
