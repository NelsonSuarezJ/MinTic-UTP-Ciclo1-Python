def hola():
    return 'Mensaje hola'


def mundo():
    return 'Mensaje mundo'


def saludo(laFuncion):  # funcion de orden superior
    resultado = laFuncion()
    print(resultado)

#le paso como parametro el nombre de la funcion
saludo(hola)
