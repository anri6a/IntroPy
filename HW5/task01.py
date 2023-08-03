# Напишите функцию f, которая на вход принимает два числа a и b,
# и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.
#
# def f(a, b):
#     degree = 1
#     res = 0
#     while < b+1:
#         res = a * f(a, b-1)
#
#     return
#
# print(f(3, 3))

def power(a, b):
    while b != 1:
        res = a * power(a, b - 1)
        return (res)
    return (a)
power(3, 5)

# def power(a, b):
#     # if (b == 1):
#     #     return (a)
#     # if (b != 1):
#         res = a * power(a, b - 1)
#         print(res)
#         return (res)