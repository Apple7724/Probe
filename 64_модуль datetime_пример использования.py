import datetime as dt


# Старт Гагарина - взлёт : 1961 год, 12 апреля, 9 часов утра, 7 минут 
start_time = dt.datetime(1961, 4, 12, 9, 7, 0)
    
print(start_time)
# текущее время и дата UTC
now = dt.datetime.utcnow()
print (now)

# текущее время и дата местное
now = dt.datetime.utcnow()
delta = dt.timedelta(hours=7)
Krasnoyarsk_time = now + delta
print (Krasnoyarsk_time)

# Расчет разности между переменными datetime
start_time = dt.datetime(2011, 4, 17)  # дата выхода первой серии
final_time = dt.datetime(2019, 4, 15)  # впишите дату выхода последней серии
    
duration = final_time - start_time   # вычислите, сколько времени шёл сериал
    
print(duration)
