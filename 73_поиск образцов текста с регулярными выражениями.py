# Сначала пример без использования регулярных выражений формат номера:
# 8-ххх-ххх-хх-хх
def isPhoneNumber(text):
    if len(text) != 15:
        return False
    if text[0] != '8':# Проверка на вхождение 8"
        return False
    if text[1] != '-':# Проверка на вхождение -"
        return False    
    for i in range(2, 4):
        if not text[i].isdecimal():
            return False
    if text[5] != '-':# Проверка на вхождение -"
        return False
    for i in range(6, 8):
        if not text[i].isdecimal():
            return False
    if text[9] != '-':# Проверка на вхождение -"
        return False
    for i in range(10, 11):
        if not text[i].isdecimal():
            return False
    if text[12] != '-':# Проверка на вхождение -"
        return False
    for i in range(13, 14):
        if not text[i].isdecimal():
            return False
    return True
# Здесь отладка
print('8-923-185-14-65 - это телефонный номер')
print(isPhoneNumber('8-923-185-14-65'))
print('212850A - это телефонный номер')
print(isPhoneNumber('212850A'))
# Здесь вызов функции для работы с текстом
message = 'Позвони мне завтра по номеру: 8-999-322-22-32.А еще рабочий номер 8-934-456-78-00'

for i in range(len(message)):
    chunk = message[i:i+15]
    if isPhoneNumber(chunk):
        print('Найденный телефонный номер: '+ chunk)
print('Готово')

# Теперь тоже с поиском по шаблону. Импортируем библиотеку Regex:
import re
# создаем шаблон с именем phoneNumRegex методом compile:
phoneNumRegex = re.compile(r'\d-\d\d\d-\d\d\d-\d\d-\d\d')
# или создаем такой же шаблон с именем phoneNumRegex2 с другим синтаксисом:
phoneNumRegex2 = re.compile(r'\d-\d{3}-\d{3}-\d{2}-\d{2}')
# поиск по тексту методом search для textWithNumber
textWithNumber = phoneNumRegex.search('Мой номер телефона: 8-555-555-55-55')
# поиск по тексту методом search для textWithNumber2
textWithNumber2 = phoneNumRegex2.search('Мой номер телефона: 8-222-333-44-55')
# Вывод на экран методом group
print('Найденный телефонный номер: ' + textWithNumber.group())
print('Найденный телефонный номер: ' + textWithNumber2.group())

# Теперь тоже с разбивкой вывода по группам group():
# когда создаем шаблон, скобками разбиваем регулярное выражение
# на группы и можем выводить в зависимости от параметра метода group()
# где число - это порядковый номер группы
phoneNumRegex3 = re.compile(r'\d-(\d\d\d)-(\d\d\d-\d\d-\d\d)')
textWithNumber = phoneNumRegex3.search('Мой номер телефона: 8-391-257-47-32')
print('телефонный код: ' + textWithNumber.group(1))
print('Найденный номер: ' + textWithNumber.group(2))
print('Весь номер: ' + textWithNumber.group(0))
print('Весь номер: ' + textWithNumber.group())
# тоже для извлечения всех групп вместе или по отдельности:
code, number = textWithNumber.groups()
print(code)
print(number)
# использование метода findall:
print(phoneNumRegex.findall(message))
# тоже, если есть группы:
print(phoneNumRegex3.findall(message))

# создаем свой символьный класс:
vowelRegex = re.compile(r'[a-zA-Z]')
vowelRegex1 = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Hello world'))
print(vowelRegex1.findall('Hello world'))
# создаем инвертируемый символьный класс добаваляя символ ^:
vowelRegex2 = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex2.findall('Hello world'))


