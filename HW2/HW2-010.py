#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
#вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
from random import randint
n = int(input('введите количество монет - '))
countMinCoin = 0
for i in range(n):
    curentCoin = randint(0,1)
    print(curentCoin)
    if curentCoin == 0: countMinCoin +=1
if countMinCoin <= n//2: print(f'перевернуть {countMinCoin} монет')
else: print(f'перевернуть {n - countMinCoin} монет')