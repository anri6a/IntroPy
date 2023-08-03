# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
import random
#5

import random
def fill_list(element):
    new_list = []
    for i in range(element):
        new_list.append(random.randint(1, 20))
    return new_list


first_set = int(input("Введите количество элементов в 1 наборе: "))
n = fill_list(first_set)
print(n)
print()
second_set = int(input("Введите количество элементов во 2 наборе: "))
m = fill_list(second_set)
print(m)

print()
print(f"Новый набор по возрастанию: {sorted(set(n + m))}")