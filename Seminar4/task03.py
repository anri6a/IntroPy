#вводятся числа последовательно пока не введется 0, тогда ввод останавливается и выводится максимальное число
import math
n = int(input())
max_number = -math.inf
while n != 0:
    n = int(input())
    if n > max_number:
        max_number = n
print(max_number)