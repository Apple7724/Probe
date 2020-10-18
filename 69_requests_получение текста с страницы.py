import requests

response = requests.get('https://ya.ru/white')

print(response.text)  # печатаем текст запрошенной страницы объем большой

# Ещё пример про запрос погоды в Красноярске

url = 'http://wttr.in/Krasnoyarsk?0T'

response = requests.get(url)  # выполните HTTP-запрос

print(response.text)  # напечатайте текст HTTP-ответа

# Ещё пример. Передаем параметры в URL

url = 'https://wttr.in'  # не изменяйте значение URL

# здесь первый параметр 0 или 1 или 2 и т.д. означает количество выводимых дней
# M - параметр для вывода в м/с, а lang -  чтобы на русском языке
# справка по этому сайту в документации https://wttr.in/:help?lang=ru
weather_parameters = {
    '2': '',
    'T': '',
    'M': '',
    'lang': 'ru'
    # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
}

response = requests.get(url, params=weather_parameters)  # передайте параметры в http-запрос

print(response.text)

# тот же результат -получаем заголовок на русском языке. Убрали из параметров,
# но поставили
# в аргументы функции get:

import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
     'M': ''
}

request_headers = {
    'Accept-Language': 'ru'# заполните словарь с заголовками
}

# не забудьте передать параметры и заголовки в http-запрос
# через аргументы `params` и `headers` функции get()
response = requests.get(url, params=weather_parameters, headers=request_headers)
print(response.text)
