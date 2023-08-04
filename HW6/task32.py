# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

max_num = int(input('max number - '))
min_num = int(input('min number - '))
work_list = [random.randint(-10, 10) for i in range(20)]
print(*work_list)
print(*[i for i in range(len(work_list)) if work_list[i]<=max_num and work_list[i]>=min_num])
# for i in range(len(work_list)):
#     if work_list[i]<=max_num and work_list[i]>=min_num:
#         print(i)
    # print(work_list.index(i<max_num))
