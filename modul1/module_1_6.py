my_dict = {'oleg': 2004,
            'saha': 2002,
            'pasha': 2001,
            'sofa': 2000}
print('Cловарь my_dict:', my_dict)
print('Год рождения oleg:', my_dict['oleg'])
print('год рождения vania:', my_dict.get('vania', 'Ключ не найден'))
my_dict.update({'sonia': 1990, 'dima': 1999})
print(my_dict)
a = my_dict.pop('sofa')
print('Удалённая пара sofia', a)
print('Обновлённый словарь my_dict', my_dict)

my_set = {1,1,1,2,2,3,3,4,4}
print('Множества my_set', my_set)
my_set.add(5)
my_set.add(6)
e = my_set.pop()
print('Удалённый элемент my_set', e)
print('Изменённое множество my_set', my_set)
