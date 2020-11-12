import pandas as pd# импорт библиотеки pandas
df = pd.read_csv(r"C:\Users\Ильгиз\AppData\Local\Programs\Python\Python38-32\phones.csv")# считываем csv файл 
phones_head = df.head(5)# сюда сохраняем пять строчек с начала данных
phones_tail = df.tail(10)# сюда сохраняем десять строчек с конца данных
print(phones_head)# печать пяти строчек начала таблицы
print(phones_tail)# печать десяти строчек конца таблицы


df = pd.read_csv('music_log.csv')
genre_fight = df[['genre', 'Artist']]
genre_pop = genre_fight[genre_fight['genre']=='pop']['genre'].count()
genre_rock = genre_fight[genre_fight['genre']=='rock']['genre'].count()
print('Число прослушанных треков в жанре поп равно',genre_pop)
print('Число прослушанных треков в жанре рок равно',genre_rock)
if genre_pop > genre_rock:
    print("Попса forever!")
else:
    print("Рок победил!")


rock = df[df['genre']=='rock']
rock_time = rock['total play']
rock_haters = rock_time.loc[rock_time <= 5].count()
#print('Количество пропущенных треков жанра рок равно', rock_haters)
pop = df[df['genre']=='pop']
pop_time = pop['total play']
pop_haters = pop_time.loc[pop_time <= 5].count()
#print('Количество пропущенных треков жанра поп равно', pop_haters)
rock_total = rock.shape[0]
pop_total = pop.shape[0]
rock_skip = rock_haters / rock_total
pop_skip = pop_haters / pop_total
print('Доля пропущенных композиций жанра рок равна: {:.1%}'.format(rock_skip))
print('Доля пропущенных композиций жанра поп равна: {:.1%}'.format(pop_skip))
