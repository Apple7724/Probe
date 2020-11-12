# программа парсинга телефонных номеров со страницы в формате csv
import re
import csv

# 

datafile = open('phones.csv') # открытие файла
readerfile = csv.reader(datafile) # считывание
listfile = list(readerfile) # сохранение в виде списка

phoneNumRegex = re.compile(r'\d{3}-\d{2}-\d{2}') # шаблон поиска(если знаешь)

for i in listfile:
    print(phoneNumRegex.findall(str(i))) # вывод телефонных номеров

#print(listfile)
