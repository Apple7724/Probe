weather = '🌡️+10°C 🌬️↑4.4m/s'
wind = weather.split()[1]
parsed_wind = ''
for char in wind:
    try:
        num = int(char)
        parsed_wind += char    
    except ValueError:
        continue
print(parsed_wind)
# будет напечатано: 44

# Поиск точки в числе:

weather = '🌡️+10°C 🌬️↑4.4m/s'
wind = weather.split()[1]
parsed_wind = ''
for char in wind:
    # проверяем каждый символ: "а не точка ли это?"
    if char == '.':
        parsed_wind += char
    try:
        num = int(char)
        parsed_wind += char
    except ValueError:
        continue
print(parsed_wind)
# будет напечатано: 4.4

# Проверка условия для прыжка:

weather = '🌡️+10°C 🌬️↑4.4m/s'
wind = weather.split()[1]
parsed_wind = ''
for char in wind:    
    if char == '.':
        parsed_wind += char
    try:
        num = int(char)
        parsed_wind += char
    except ValueError:
        continue
# приводим parsed_wind к числу с плавающей точкой — и после этого сравниваем
if float(parsed_wind) < 5:
    print('Можно прыгать!')
else:
    print('Не прыгай, дует!') 
# будет напечатано: Можно прыгать!
