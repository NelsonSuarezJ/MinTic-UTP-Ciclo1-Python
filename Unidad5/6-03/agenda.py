import pandas as pd
from pandas.core.frame import DataFrame


def list_contacts():
    print(get_df())


def get_df():
    return pd.read_csv('contacts.csv')


def save_df(new_df: DataFrame):
    new_df.to_csv('contacts.csv', index=False)


def find_word():
    palabra = input('Digita la palabra a buscar')
    df = get_df()
    print(df[df["name"].str.contains(palabra)])


def update_contact():
    list_contacts()
    id = int(input('Id de contacto: '))
    option = input("""Que desea editar?
                   1- Nombre
                   2- Celular
                   3- E-mail
                   """)
    data = get_df()
    if option == '1':
        data.loc[id, 'name'] = input('Nombre: ')
    elif option == '2':
        data.loc[id, 'cel'] = input('Celular: ')
    elif option == '3':
        data.loc[id, 'mail'] = input('E-mail: ')
    save_df(data)


def delete_contact():
    list_contacts()
    id = int(input('Id de contacto: '))
    data = get_df()
    data.drop([id], inplace=True, axis=0)
    save_df(data)


def create_contact():
    name = input('Nombre: ')
    cel = input('Celular: ')
    mail = input('E-mail: ')
    fr = open('contacts.csv', 'a')
    fr.write(f'{name},{cel},{mail}\n')
    fr.close()


def show_menu():
    print(
        """ Menu
        1- Crear
        2- Listar
        3- Buscar
        4- Editar
        9- Salir""")
    option = input('Digite la opción: ')
    if option == '1':
        create_contact()
    elif option == '2':
        list_contacts()
    elif option == '3':
        find_word()
    elif option == '4':
        update_contact()
    elif option == '5':
        delete_contact()
    elif option == '9':
        exit()


def run():
    show_menu()
    run()


if __name__ == '__main__':
    # df = pd.DataFrame(columns=['name','cel','mail'])
    # df.to_csv('contacts.csv')
    run()
