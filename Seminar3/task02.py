# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю
# последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
from random import randint
n = int(input('введите количество чисел - '))
k = int(input('введите размер сдвига - '))
list = [randint(-5,5) for i in range(10)]
print(list)

# for i in range(k):
#     list.insert(0, list.pop())
# print(list)

print(list[len(list)-k:] + list[:len(list)-k])