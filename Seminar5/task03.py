# 1. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)*
# from random import randint
# num = randint(1, 100)
# print(num)
# flag = False
# for i in range(2, num-1):
#     if num % i == 0:
#         flag = True
# if flag == False:
#     print('yes')
# else:
#     print('no')

def is_prime(num: int) -> bool:
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for dev in range(3, num // 2 + 1, 2):
        if num % dev == 0:
            return False
    return True

