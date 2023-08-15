# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
#   print(‘same’)
# else:
#   print(‘different’)

values = [0, 2, 10, 6]

def same_by(func, lst_obj):
    return len(set(map(func, lst_obj))) < 2

print(same_by(lambda x: x%2 == 0, values))

if same_by(lambda x: x%2 == 0, values):
    print('same')
else: print('different')

print('same' if same_by(lambda x: x%2 == 0, values) else 'different')