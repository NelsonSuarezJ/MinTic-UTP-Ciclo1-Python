def mayorDeTresNumeros(centenas, decenas, unidades):
    mayor = centenas
    posicion = 0
    if centenas > decenas and centenas >= unidades:
        mayor = centenas
        posicion = 1
    elif decenas > centenas and decenas >= unidades:
        mayor = decenas
        posicion = 2
    elif unidades > decenas and unidades >= centenas:
        mayor = unidades
        posicion = 3
    return mayor, posicion


def esPrimo(numero):
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    return primo


def centenasDecenasUnidades(numero):
    unidades = numero % 10
    decenas = (numero % 100) // 10
    centenas = numero//100
    return centenas, decenas, unidades


def decenasUnidades(numero):
    unidades = numero % 10
    decenas = numero//10
    return decenas, unidades
