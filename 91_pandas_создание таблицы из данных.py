import pandas as pd
# исходные данные в переменной atlas.
# задача - создать из них таблицу из двух колонок
# с названием country и capital
atlas = [
    ['Франция','Париж'],
    ['Россия','Москва'],
    ['Китай','Пекин'],
    ['Мексика','Мехико'],
    ['Египет','Каир'],
]
geography = ['country', 'capital'] # в переменную сохраняем шаблон таблицы 
# (количество столбцов и их наименования)
# таблица сохраняется в переменной с произвольно выбранным именем world_map:
world_map = pd.DataFrame(data = atlas , columns = geography)

print(world_map) # вывод на экран



music = [
    ['Radiohead','Creep'],
    ['Queen','Bohemian Rhapsody'],
    ['Ария','Беспечный ангел'],
    ['Юрий Визбор','Три Минуты Тишины'],
    ['AC/DC','Highway to Hell']
]
entries =['artist', 'track']
playlist = pd.DataFrame(data=music, columns=entries)
print(playlist)
