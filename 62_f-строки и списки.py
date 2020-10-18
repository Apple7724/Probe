def calc_stat(listened):  # от англ. calculate statistics, посчитать статистику
        # напишите код функции calc_stat
    n = len (listened)
    global m, s
    m = 0
    s = 0
    for i in range(len(listened)):
        minutes = listened[i]//60
        seconds = listened[i]%60
        m = m + minutes
        s = s + seconds
    m = m + s//60
    s = s%60
    text = f'Вы прослушали {n} песен, общей продолжительностью {m} минут и {s} секунд.'
    return text
        
print(calc_stat([193, 148, 210, 144, 174, 159, 163, 189, 230, 204]))
