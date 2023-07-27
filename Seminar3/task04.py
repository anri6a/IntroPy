# Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
from random import randint
n = int(input('введите количество чисел - '))
lst = [randint(0, 10) for i in range(n)]
print(lst)
#count = 0
# for i in range(len(lst)-1):
#     if lst[i+1] > lst[i]:
#         count += 1
# print(count)
print(len([lst[i] for i in range(1, len(lst)) if lst[i-1] < lst[i]]))
#print([lst[i] for i in range(1, len(lst)) if lst[i-1] < lst[i]])
