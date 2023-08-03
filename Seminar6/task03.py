# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
import random
n = int(input('enter number - '))
list1 = [random.randint(-5, 10) for i in range(n)]
print(list1)
counter = 0
for i in set(list1):
    counter += list1.count(i)//2
print(counter)
print(sum([list1.count(i)//2) for i in set(list1)]))