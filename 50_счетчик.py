may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]
may_2018 = [20, 27, 23, 18, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25, 21, 17, 11, 20, 21, 22, 23, 18, 20, 23, 18, 22, 23, 11]

# допишите код ниже
def comfort_count(temperatures):
    n = 0
    for temp in range(len(temperatures)):
        if temperatures[temp] >= 22 and temperatures[temp] <= 26:
            n = n + 1
            print(temp,temperatures[temp],n)
    print('Количество комфортных дней в этом месяце: ', n)
# дальше код не меняйте
comfort_count(may_2017)  # узнаем, что было в мае 2017 г.
comfort_count(may_2018)  # узнаем, что было в мае 2018 г.
