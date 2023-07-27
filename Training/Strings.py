name = "hi there"
first_name = "andrei"
second_name = "shyrakou"
full_name = first_name + " " +second_name #concatenate
print(name.title()) #Заглавные в каждом слове
print(name.lower()) #строчные ВСЕ
print(name.upper()) #заглавные ВСЕ 
print('Hello, ' + full_name.title() + "!") #concatenate
print('Python')
print('\tPython')
print('\tPython is \n\tgood language')
strWithSpaces = ' string with spaces '
strWithSpaces.rstrip() #удаление пробелов в конце строки
strWithSpaces.lstrip() #удаление пробелов в начале строки
strWithSpaces.strip #удаление пробелов в начале и конце строки
strWithSpaces.split() #разделение строки
strWithSpaces.replace('.', ' ') #замена символов
a = 3
b = 11
s = 2022
print(a, b, s)
print(a,'-', b,'-', s)
print('{} - {} - {}'.format(a,b,s))
print(f'first - {a} second - {b} third - {s}')
a = 1.43425
b = 2.2983
c = round(a * b, 5) # округление до 5 знаков после запятой
print(c)

