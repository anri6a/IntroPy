#Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
import math
list_1 = [1, 2, 3, 4, 5, 10, 8, 20]
k = 16
max_number = math.inf
for i in range(len(list_1)):
    if abs(list_1[i]-k) < max_number:
        max_number = abs(list_1[i]-k)
        nearest = list_1[i]
print(nearest)
