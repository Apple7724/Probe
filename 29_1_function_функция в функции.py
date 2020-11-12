# Еще одна программа (функция в функции):

def positive():
    print('Positive')

def negative ():
    print('Negative')

def test ():
    k = int(input('Input integer number '))
    if k > 0:
        positive()
    else:
        negative()

test()

# ещё пример:

def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '!' # метод возвращает буквы нижнего регистра
    def yell(text):
        return text.upper() + '!' # метод возвращает буквы верхнего регистра
    if volume > 0.5:
        return yell
    else:
        return whisper

speak = get_speak_func(0.6)# переменной speak присваиваем свойство
# объекта-функции yell. Потому что условие > 0.5
# Как бы заводим функцию speak такую же как yell

print(speak('Hello'))# печать результата вызова функции speak

# Еще код с использованием лексического замыкания (здесь надо ООП штудировать)
# Сравнить с предыдущим кодом написание:
def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '!'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

result = get_speak_func('Hello',0.6)() # Вот эта конструкция непонятна пока(ООП)
print(result)
