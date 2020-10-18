# здесь подключите библиотеку random и дайте ей краткое имя
import random as r

answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']


def how_are_you():
    # напишите ваш код здесь
    a = r.choice(answers)
    return a

print(how_are_you())
