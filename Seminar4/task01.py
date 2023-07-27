#Напишите программу, которая принимает на вход строку и отслеживает сколько раз встречается каждый символ.
#ЯКоличество повторов добавдяется к символам с помощью постфикса формата _n
number = input('введите число -')
work_dict = {}
result = []
for i in number:
    work_dict[i] = work_dict.get(i, 0)+1
    # print(work_dict)
    result.append(f'{i}'+(f'_{work_dict[i]-1}' if work_dict[i] > 1 else ''))
#   print(f'{i}'+(f'_{work_dict[i]-1}' if work_dict[i] > 1 else ''), end = ' ')
print(*result) # * - выводит чистые элементы
