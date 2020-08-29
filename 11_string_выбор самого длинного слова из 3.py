first = input('введите название города №1 ')
second = input('введите название города №2 ')
third = input('введите название города №3 ')
if len(first) > len(second) and len(first) > len(third):
    print ('самое длинное название - ', first)
elif len(second) > len(first) and len(second) > len(third):
    print ('самое длинное название - ', second)
else:
    print ('самое длинное название - ', third)
