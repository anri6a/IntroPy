# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Функция не должна ничего выводить, только возвращать значение.
def sum(a, b):
    if(a<b):
        return sum(b, a)
    if (a!=0):
        res = 1 + sum(a-1, b)
        print(res)
        return res
    else:
        return (0)
print(sum(11, 13))
