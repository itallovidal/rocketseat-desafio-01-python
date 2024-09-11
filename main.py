import operations

print("Bem vindo à sua Agenda.\n")
contact_list = []


def choose_contact():
    while True:
        operations.view_contact_list(contact_list)
        chosen_contact = int(input("Escolha um contato:"))
        list_size = len(contact_list)

        if chosen_contact == list_size or list_size > chosen_contact > 0:
            return int(chosen_contact)

        print("Escolha um contato da lista.")


while True:
    print("\nEscolha uma opção:\n")
    print("1 - Adicionar contato novo:")
    print("2 - Visualizar lista de contatos:")
    print("3 - Editar um contato:")
    print("4 - Marcar/desmarcar contato  como favorito:")
    print("5 - Apagar um contato:")
    print("6 - Sair:")

    option = input("\nOpção: ")

    match option:
        case '1':
            operations.add_contact(contact_list)
            print("contato adicionado com sucesso!")
        case '2':
            operations.view_contact_list(contact_list)
        case '3':
            contact_index = choose_contact()
            operations.edit_contact(contact_list, contact_index)
        case '4':
            contact_index = choose_contact()
            operations.change_favorite_status(contact_list, contact_index)
        case '5':
            contact_index = choose_contact()
            operations.delete_contact(contact_list, contact_index)
        case '6':
            print("Até mais!")
            break

        case _:
            print("Escolha inválida")
