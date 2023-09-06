menu = ['главное меню',
        'открыть файл',
        'сохранить файл',
        'показать контакты',
        'создать контакт',
        'найти контакт',
        'изменить контакт',
        'удалить контакт',
        'выход']
input_menu = 'выберите пункт меню: '
input_menu_error = f'ввести нужно ЧИСЛО (от 1 до {len(menu) - 1})'
load_successful = 'телефонная книга загружена успешно'
save_successful = 'телефонная книга сохранена успешно'
empty_book_error = 'телефонная книга пуста или не открыта'
input_contact = ['введите имя нового контакта: ',
                 'введите номер телефона: ',
                 'введите комментарий: ']

input_edit_contact = ['введите новое имя или нажмите ENTER: ',
                      'введите номер телефона или нажмите ENTER: ',
                      'введите комментарий или нажмите ENTER: ']
input_search_word = 'Введите ключевое слово для поиска: '

operation = ['создан', 'изменен', 'удален']


def contact_action(name: str, action: str) -> str:
    return f'контакт {name} успешно {action}!'


input_edit_contact_id = 'Введите номер контакта для изменения: '
input_dell_contact_id = 'Введите номер контакта для удаления: '


def not_find(word: str) -> str:
    return f'Контакты содержащие "{word}" не найдены!'

exit_program = 'До свидания! До новых встреч!'