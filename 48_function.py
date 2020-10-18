def print_friends_count(friends_count, name=''):
    # добавьте новый аргумент
    if friends_count == 1:
        text = '1 друг'
    elif 2 <= friends_count <= 4:
        text = str(friends_count) + ' друга'
    elif friends_count >= 5:
        text = str(friends_count) + ' друзей'
    if name != '':
        print(name, ', у тебя ', text)
    else:
        print('У тебя ', text)


# дальше код не меняйте
print_friends_count(3, 'Артём')
print_friends_count(friends_count=7, name='Марина')
print_friends_count(6)
print_friends_count(4, name='Настя')
