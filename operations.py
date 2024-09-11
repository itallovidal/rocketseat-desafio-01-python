import re
from typing import Tuple


class Contact:
    __is_favorite: bool

    def __init__(self, name, phone_number, email):
        self.__name = name
        self.__phone_number = phone_number
        self.__email = email
        self.__is_favorite = False

    def change_name(self, new_name):
        self.__name = new_name

    def change_phone_number(self, new_phone):
        self.__phone_number = new_phone

    @staticmethod
    def verify_email(email) -> bool:
        while True:
            email_regex = r"^[\w\.-]+@[\w-]+\.[a-zA-Z]{2,}$"
            if re.match(email_regex, email):
                return True

            email = input("Email inválido, digite novamente ou digite 1 para desistir.")

            if email == "1":
                return False

    @staticmethod
    def verify_name(name) -> bool:
        while True:
            if len(name) > 2:
                return True

            email = input("Nome inválido, digite um nome com mais de 2 caracteres, ou digite 1 para desistir.")

            if email == "1":
                return False

    def change_email(self, new_email) -> Tuple[bool, str]:
        is_success = self.verify_email(new_email)

        if is_success:
            self.__email = new_email
            return True, "Atualizado com sucesso!"

        return False, "Sem problemas, atualize o email mais tarde!"

    def is_favorite(self):
        return self.__is_favorite

    def change_favorite_status(self):
        self.__is_favorite = not self.__is_favorite

    def info(self):
        return f"{"🤍" if self.__is_favorite else ""}  {self.__name} - {self.__phone_number} - {self.__email}"


def add_contact(contact_list: list):
    name = input("Digite o nome do contato:\n")
    is_name_correct = Contact.verify_name(name)

    if not is_name_correct:
        print("Operação cancelada.")
        return

    email = input("Digite o email do contato:\n")

    is_email_correct = Contact.verify_email(email)
    if not is_email_correct:
        print("Operação cancelada.")
        return

    phone_number = input("Digite o telefone:\n")

    new_contact = Contact(name, phone_number, email)
    contact_list.append(new_contact)
    return


def view_contact_list(contact_list: list):
    if len(contact_list) == 0:
        print("Lista de contatos vazia!\n")
        return

    for index, contact in enumerate(contact_list):
        print(f"{index + 1} - {contact.info()}")

    print("\n")

    return


def edit_contact(contact_list: list, contact_index: int):
    contact: Contact = contact_list[contact_index - 1]
    while True:
        print("1 - Nome")
        print("2 - Email")
        print("3 - telefone\n")
        chosen_opc = input("O que deseja editar? ")

        match chosen_opc:
            case "1":
                new_name = input("\nDigite o novo nome:")
                contact.change_name(new_name)
                break

            case "2":
                new_email = input("\nDigite o novo email:")
                (isSuccess, message) = contact.change_email(new_email)
                print(message)
                break
            case "3":
                new_phone = input("\nDigite o novo telefone:")
                contact.change_phone_number(new_phone)
                break
            case _:
                print("Digite uma opção válida.")

    print(contact.info())


def change_favorite_status(contact_list: list, contact_index: int):
    contact: Contact = contact_list[contact_index - 1]
    contact.change_favorite_status()
    print("\nStatus atualizado com sucesso!\n")
    print(contact.info())


def delete_contact(contact_list: list, contact_index):
    contact: Contact = contact_list[contact_index - 1]
    contact_list.remove(contact)
    print("Contato removido com sucesso!\n")
    view_contact_list(contact_list)
