names = ['Саня', 'Ваня', 'Валек']
names.append('женя')
print(names)
message = 'at first i met ' + names[2] + ' then ' + names[0] + ' and ' + names[1] +\
          ' and not so long ago ' + names[3].title() + '!'
print(message)
names.insert(0, 'кирилл')
print(names)
del names[2]
print(names)
popped_names = names.pop() #удаление и сохранение последнего элемента списка. pop(2)-для выбранного элемента
print(popped_names.title())
names.remove('кирилл')
print(names)
names.append('женя')
names.append('костя')
names.sort(reverse=True) #сортировка в порядке убывания
print(sorted(names)) #временно сортирует список без сохранения
print(len(names))
names.reverse() #переходит к обратному порядку списка





