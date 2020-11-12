# данная программа выводит прогноз погоды для заданного
# наcеленного пункта
import json, requests, sys
# Определение названия населенного пункта из аргументов
# командной строки
if len(sys.argv) < 2:
    print('Использование: программы....')
    sys.exit
location = ''.join(sys.argv[1:])
# Загрузить json-данные из API сайта OpenWeatherMap.org
url = 'https://openweathermap.org/find?q=krasnoyarsk'
#url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()
weather = json.dumps(response.text)
print(weather[0:3000])



