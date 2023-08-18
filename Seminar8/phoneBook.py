# написать телефонный справочник Имя Фамилия; телефон; комментарий
# 0. открыть справочнок
# def open_phone_book_menu(file_name)
# 1. вывести все записи на экран
# def print_all_phone_book(file_name)
# 2. добавить контакт
# def add_new_contact(file_name)
# 3. изменить контакт
# def edit_contact(file_name)
# 4. удалить контакт
# def remote_contakt(file_name)
# 5. найти контакт
# def find_contact(file_name)


# Андрей Ширяков;5568654;заместитель
# Сергей Рабчун;7653819;связист
# Александр Еремейчик;8303044;диспетчер
# Андрей Лазарь; 5567865;инженер
# Сергей Сновалов;5678754;водитель
# Алексей Свирид;09823478;диспетчер
#______________________________________________________________________
import os


def open_phone_book_menu():
    selected_operation = ''
    while selected_operation != 6:
        selected_operation =int(input('\n Введите желаемую операцию:\n'
          '1 - вывести все контакты на экран;\n'
          '2 - добавить новый контакт\n'
          '3 - изменить существующий контакт\n'
          '4 - удалить контакт\n'
          '5 - найти контакт\n'
          '6 - закончить работу со справочником\n'
          'ваш выбор - '))
        if selected_operation == 1:
            print_all_phone_book('phones.txt')
        if selected_operation == 2:
            add_new_contact('phones.txt')
        if selected_operation == 3:
            edit_contact('phones.txt')
        if selected_operation == 4:
            remove_contakt('phones.txt')
        if selected_operation == 5:
            find_contact('phones.txt')

def print_all_phone_book(file_name):
    with open(file_name, 'r', encoding='utf-8') as date_phones:
        date_phones = date_phones.readlines()
        date_phones = list(map(lambda x: x.strip().replace(';', ' '), date_phones))
        print('\n'.join(date_phones))


def add_new_contact(file_name):
    with open(file_name, 'a', encoding='utf-8') as date_phones:
        new_contact = input('введите Имя Фамилию;телефон;комментарий для нового контакта - ')
        date_phones.write('\n'+new_contact)


def edit_contact(file_name):
    date_work = open('phones.txt', 'r', encoding='utf-8')
    date_phones = date_work.readlines()
    date_work.close()

    line_to_edit = input('введите фамилию контакта, который нужно изменить: ')
    search_line = list(filter(lambda x: line_to_edit in x, date_phones))
    print(search_line)
    date_to_edit = input('введите что поменять - ')
    date_to_update = input('введите на что поменять - ')
    print(f'заменить "{date_to_edit.upper()}" на "{date_to_update.upper()}"')
    for line in range(len(date_phones)):
        if date_to_edit in date_phones[line]:
            date_phones[line] = date_phones[line].replace(date_to_edit, date_to_update)
            #print(date_phones[line])
    date_work = open('phones.txt', 'w', encoding='utf-8')
    date_work.writelines(date_phones)
    date_work.close()


def remove_contakt(file_name):
    with open(file_name, 'r', encoding='utf-8') as source, open('out.txt', 'w', encoding='utf-8') as dest:
        line_to_remove = input('введите контакт для удаления - ')
        for line in source:
            if line_to_remove not in line:
                dest.write(line)
    os.remove(file_name)
    os.rename('out.txt', 'phones.txt')

def find_contact(file_name):
    with open(file_name, 'r', encoding='utf-8') as data_phones:
        line_to_find = input('введите контакт для поиска - ')
        for line in data_phones:
            if line_to_find in line:
                print(line)

open_phone_book_menu()
