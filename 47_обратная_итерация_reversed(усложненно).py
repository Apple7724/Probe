messages_count = 10
count = [count for count in range(2, messages_count+1)]
back = reversed(count)
for i in back:
    print('- Анфиса, есть ли новые письма?')
    print('- Непрочитанных писем:', i,end='.\n')
    print('Я прочитал одно, и их осталось', i-1,end='.\n')
print('- Анфиса, есть ли новые письма?')
print('- Одно непрочитанное письмо.')
print('Я прочитал его. И нет больше писем!')
