# Дан список чисел. Определите, сколько в нем встречается различных чисел.
from random import randint
n = int(input('введите количество чисел - '))
list1 = [randint(-5, 5) for i in range(n)]
print(list1)
print(set(list1))
print(f'различных чисел {len(set(list1))}')
#print(set([randint(-5, 5) for i in range(n)]))