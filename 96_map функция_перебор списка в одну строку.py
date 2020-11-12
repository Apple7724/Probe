data = [
    ['model', 'Mersedes Benz', 'GLK'],
    ['model', 'BMW', 'X6'],
    ['model', 'Honda', 'Accord'],
    ]

def func(text):
    return text.upper()# функция переводит символы 
# в верхний регистр методом upper()

#  пройти по всем данным( с помощью цикла):
for i in data:
    print(list(map(func,i)))



    
