devs = [{"nombre": "nelson", "salario": 100, "cc": 123},
        {"nombre": "enrique", "salario": 200, "cc": 456}]


def createCRUD():
    dev = dict(nombre='', salario=0)
    nombre = input("Ingrese nombre: ")
    salario = int(input("Ingrese salario: "))
    cedula = int(input("Ingrese cedula: "))
    dev['nombre'] = nombre
    dev['salario'] = salario
    dev['cc'] = cedula
    devs.append(dev)
    run()


def buscarDevPorCc():
    cedula = int(input("Ingrese cedula del desarrolador: "))
    noEncontrado = True
    for d in devs:
        if cedula == d['cc']:
            print(f"Nombre: {d['nombre']}, Salario {d['salario']}")
            noEncontrado = False
            break
    if noEncontrado:
        print("Ningun desarrollador con esa cedula")
    run()


def listarCRUD():
    print("Lista de desarrolladores: ")
    for i in devs:
        print(f"Nombre: {i['nombre']}, Salario: {i['salario']}, Cedula:{i['cc']}")
    run()


def opciones():
    print("""Escoga una opcion:
        1. Crear un Desarrollador
        2. Listar Desarrolladores
        3. Buscar desarrollador por cedula
        9. Salir""")
    option = input()
    return option


def run():
    opc = opciones()
    if opc == "1":
        createCRUD()
    elif opc == "2":
        listarCRUD()
    elif opc == "3":
        buscarDevPorCc()
    else:
        exit()
