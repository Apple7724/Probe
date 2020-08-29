word = input('введите слово ')
number = len(word)
while number > 0:
    print (word[number-1],end = '')
    number = number -1
