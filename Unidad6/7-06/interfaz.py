# se instala libreria pip install easygui
import easygui as eg
import poo as cl

biblioteca = cl.Biblioteca('Alejandria')


def menu():
    msg = 'Menu de opciones'
    title = f'Biblioteca {biblioteca.name}'
    choices = ['Agregar sala', 'Listar salas']
    window = eg.buttonbox(msg, title, choices)
    if window == None:
        eg.msgbox('Gracias por preferirnos!')
    elif window == choices[0]:
        add_room()
    elif window == choices[1]:
        list_rooms()


def menu_room(index):
    msg = 'Menu de opciones'
    title = f'Biblioteca {biblioteca.name} -> Sala {biblioteca.rooms[index].name}'
    choices = ['Agregar libro', 'Listar libros']
    window = eg.buttonbox(msg, title, choices)
    if window == None:
        eg.msgbox('Gracias por preferirnos!')
    elif window == choices[0]:
        pass
        # add_book()  # falta crear esta función
    elif window == choices[1]:
        pass
        # list_books()  # falta crear esta función


def list_rooms():
    msg = 'Listado de salas'
    title = 'Biblioteca -> salas'
    choices2 = biblioteca.get_rooms()
    option = eg.indexbox(msg, title, choices=choices2)
    if option == None:
        menu()
    else:
        menu_room(option)


def add_room():
    msg = 'Agregar una sala'
    title = 'Biblioteca -> sala'
    field_names = ['Nombre', 'Capacidad']
    field_values = []
    field_values = eg.multenterbox(msg, title, field_names)
    if field_values == None:
        menu()
    elif field_values[0] == '' or field_values[1] == '':
        eg.msgbox('Debe llenar los campos!')
        add_room()
    else:
        biblioteca.add_room(field_values[0], field_values[1])
        menu()


if __name__ == '__main__':
    menu()
