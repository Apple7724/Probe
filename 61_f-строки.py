weather = 'облачно'
print(f'На улице сейчас {weather}.')
    
# Сравните с
# print('На улице сейчас ' + weather + '.')
# или
# print('На улице сейчас', weather, '.') — в таком коде не убрать
# пробел перед точкой
one_hundred = 100
rubles = 'рублей'
friends = 'друзей'
print(f'Не имей {one_hundred} {rubles}, а имей {one_hundred} {friends}.')

# Это проще и понятнее, чем написать
# print('Не имей ' + str(one_hundred) + ' ' + rubles + ', а имей ' + str(one_hundred) +' ' + friends + '.') 


# в функции:

def show_meteo(temperature, weather):
    print(f'Сейчас {weather}, на градуснике {temperature}.')

# в условии и в цикле:

show_meteo(24, 'облачно')

def format_text(messages_count):
    remainder = messages_count % 10
    if messages_count == 0:
        return 'нет новых сообщений'
    elif remainder == 0 or remainder >= 5 or (10 <= messages_count <= 19):
        return f'{messages_count} новых сообщений'
    elif remainder == 1:
        return f'{messages_count} новое сообщение'
    else:
        return f'{messages_count} новых сообщения'

    
def print_count(messages_count):
    text = format_text(messages_count)
    print(f'У вас {text}.')

    
print_count(0)
print_count(1)
print_count(4)
print_count(5)
print_count(12)
print_count(22)
print_count(25)

def print_time(hour, minute, second):
    print (f'{hour}:{minute}:{second}')  # аргумент должен содержать f-строку

    
print_time('19', '28', '06')
