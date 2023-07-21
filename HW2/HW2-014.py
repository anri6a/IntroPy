#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
#не превосходящие числа N.
n = int(input('введите максимальное число - '))
res = 0
i = 0
flag = True

while flag:
    print(res)
    res = 2**i
    i += 1
    if res > n:
        flag = False

    
