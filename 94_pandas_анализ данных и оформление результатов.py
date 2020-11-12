import pandas as pd
df = pd.read_csv('music_log_upd.csv')
# группировка по столбцу 'user_id' без использования метода получаем
# DataFrameGroupBy :
genre_grouping = df.groupby('user_id')
# группировка по этому же столбцу и подсчет значений 'genre_name'
# (создаем новый Series 'genre_counting', т.к столбец один)
genre_counting = df.groupby('user_id')['genre_name'].count()
# вывод на печать...
print(genre_counting.head(30))

# функция ищет данные по столбцу жанр с длиной строки больше 50:
def user_genres(group):
    for col in group:
        if len(col[1]) > 50:
            user = col[0]
            return user
# вызов функции:
search_id = user_genres(genre_grouping)
# сортировка таблицы по двум условиям:
music_user = df[(df['user_id']==search_id) & (df['total_play_seconds']!=0)]
# сортировка полученной таблицы по столбцу 'genre_name'
# и суммирование значений по столбцу 'total_play_seconds':
sum_music_user = music_user.groupby('genre_name')['total_play_seconds'].sum()
# вывод на экран:
print(sum_music_user)

# группировка по столбцу 'genre_name' подсчет значений по этому же столбцу:
count_music_user = music_user.groupby('genre_name')['genre_name'].count()
print(count_music_user)

# сортировка предпочтений по жанрам в порядке убывания,
# чтобы увидеть самое большее
final_sum = sum_music_user.sort_values(ascending=False)
print(final_sum)

# сортировка предпочтений по числу композиций в жанрах в порядке убывания,
# чтобы увидеть самое большее
final_count = count_music_user.sort_values(ascending=False)
print(final_count)

# Получаем таблицу с композициями самого популярного жанра — pop,
# исключив пропущенные треки:
pop_music = df[(df['genre_name']=='pop') & (df['total_play_seconds']!=0)]
# Находим максимальное время прослушивания песни в жанре pop
pop_music_max_total_play = pop_music['total_play_seconds'].max()
print(pop_music_max_total_play)

# Получаем строку таблицы pop_music c информацией
# о самой длинной по времени прослушивания песне жанра 'pop' 
pop_music_max_info = pop_music[pop_music['total_play_seconds'] == pop_music['total_play_seconds'].max()]
print(pop_music_max_info)

# Находим минимальное ненулевое время прослушивания композиции в жанре pop:
pop_music_min_total_play = pop_music['total_play_seconds'].min()
print(pop_music_min_total_play)

# Информация о композиции жанра pop, которую запустили,
# но быстрее всех остальных выключили:
pop_music_min_info = pop_music[pop_music['total_play_seconds'] == 
                              pop_music['total_play_seconds'].min()]
print(pop_music_min_info)

# Расчет медианы времени прослушивания произведений жанра pop:  
pop_music_median = pop_music.median()
print(pop_music_median)

# Расчет среднего ариметического времени прослушивания произведений жанра pop:
pop_music_mean = pop_music['total_play_seconds'].mean()
print(pop_music_mean)

# Находим медианное значение для суммы прослушиваний по пользователю:
# По сути находим метрику, ради которой все исследование происходило...
current_happiness = df.groupby('user_id').sum().median()
print(current_happiness)

# Выводим как результат исследований таблицу(данные вбиты...): 

data = [['pop', 8663, 34.6, 1158.03, 0.000794],
       ['rock', 6828, 33.3, 1699.14882, 0.014183]]
columns = ['genre_name','total_track','skip_track','max_total_time','min_total_time']
research_genres_result = pd.DataFrame(data=data, columns=columns)
print(research_genres_result)
