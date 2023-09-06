from model import PhoneBook
import text
import view


def search_contact(pb):
    word = view.input_request(text.input_search_word)
    result = pb.find_contact(word)
    view.show_book(result, text.not_find(word))
    if result:
        return True


def start():
    pb = PhoneBook()
    while True:
        choice = view.main_menu()
        if choice == 1:
            pb.open_file()
            view.print_message(text.load_successful)
        if choice == 2:
            pb.save_file()
            view.print_message(text.save_successful)
        if choice == 3:
            view.show_book(pb, text.empty_book_error)
        if choice == 4:
            new_contact = view.input_contact(text.input_contact())
            pb.add_contact(new_contact)
            view.print_message(text.contact_action(new_contact[0], text.operation[0]))

        if choice == 5:
            search_contact(pb)
        if choice == 6:
            if search_contact(pb):
                c_id = int(view.input_request(text.input_edit_contact_id))
                new_contact = view.input_contact(text.input_contact(True))
                name = pb.edit_contact(c_id, new_contact)
                view.print_message(text.contact_action(name, text.operation[1]))
        if choice == 7:
            if search_contact(pb):
                c_id = int(view.input_request(text.input_dell_contact_id))
                name = pb.delete_contact(c_id)
                view.print_message(text.contact_action(name, text.operation[2]))

        if choice == 8:
            if pb.original_book != pb.phone_book:
                if view.input_request(text.confirm_chnges).lower() == 'y':
                    pb.save_file
                    view.print_message(text.save_successful)
            view.print_message(text.exit_program)
            break
