import pandas as pd
df = pd.read_csv('music_log.csv')
# замена названий столбцов на новые:
new_names = ['user_id', 'total_play_seconds', 'artist_name', 'genre_name', 'track_name']
df.set_axis(new_names, axis="columns", inplace=True)
print(df.columns)

# другая таблица, продолжаем подготавливать данные:

df = pd.read_csv('music_log_upd_col.csv')
df.info()# информация о датафрейме до изменений(чистки)  
print(df.isnull().sum())# печать суммы отсуствующих значений в таблице
df['track_name'] = df['track_name'].fillna('unknown')# замена отсутствующих зна-
# чений в столбце 'track_name' на значение 'unknown'
df['artist_name'] = df['artist_name'].fillna('unknown')# тоже для столбца
#'artist_name'

df.dropna(subset=['genre_name'], inplace = True)# удаление пропущенных
# значений из столбца 'genre_name'
df.info()# информация о датафрейме после изменений(чистки)

shape_table = df.shape # текущий размер таблицы сохр. в переменную shape_table
print(df.duplicated().sum()) # печать кол-ва дубликатов
# удаляем дубликаты (строки) с переименованием
# индексов(номеров строк) по порядку (drop=True). т.к. строки удаляются
# вместе с индексами и нарушается нумерация
df = df.drop_duplicates().reset_index(drop=True)
shape_table_update = df.shape # размер новой таблицы после удаления дубликатов

if shape_table == shape_table_update:
    print('Размер таблицы не изменился, текущий размер:', shape_table_update)
else:
    print( 'Таблица уменьшилась, текущий размер:', shape_table_update)
# вывод уникальных значений в столбце 'genre_name':
print(df['genre_name'].unique())
# замена в столбце 'genre_name' значений 'электроника' на 'electronic':
df['genre_name'] = df['genre_name'].replace('электроника', 'electronic')
# подсчет количства значений 'электроника' в столбце 'genre_name' и вывод на экран
print(df.loc[df.loc[:, 'genre_name']=='электроника']['genre_name'].count())
