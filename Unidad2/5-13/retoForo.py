def cuentaLenguajes(diccionario):
    lenguajes1 = len(diccionario[1]["habilidades"]["lenguajes"])
    lenguajes2 = len(diccionario[2]["habilidades"]["lenguajes"])
    if lenguajes1 > lenguajes2:
        print(f"El desarrollador 1 sabe {lenguajes1-lenguajes2} lenguajes mas que el desarrollador 2")
    elif lenguajes2 > lenguajes1:
        print(f"El desarrollador 2 sabe {lenguajes2-lenguajes1} lenguajes mas que el desarrollador 1")
    else:
        print("Saben la misma cantidad de lenguajes")


def diferenciaLenguajes(diccionario):
    for i in diccionario[1]["habilidades"]["lenguajes"]:
        iguales = False
        for j in diccionario[2]["habilidades"]["lenguajes"]:
            lenguajes1 = diccionario[1]["habilidades"]["lenguajes"][i]
            lenguajes2 = diccionario[2]["habilidades"]["lenguajes"][j]
            if lenguajes1 == lenguajes2:
                iguales = True
        if not(iguales):
            print(f"El programador 1 sabe {lenguajes1} que no sabe el programador 2")

    for i in diccionario[2]["habilidades"]["lenguajes"]:
        iguales = False
        for j in diccionario[1]["habilidades"]["lenguajes"]:
            lenguajes1 = diccionario[1]["habilidades"]["lenguajes"][j]
            lenguajes2 = diccionario[2]["habilidades"]["lenguajes"][i]
            if lenguajes1 == lenguajes2:
                iguales = True
        if not(iguales):
            print(f"El programador 2 sabe {lenguajes2} que no sabe el programador 1")


def diferencias(diccionario):
    x = diccionario[1]['habilidades']['lenguajes']
    y = diccionario[2]['habilidades']['lenguajes']
    lenguajes = {k: y[k] for k in y if k not in x}
    return "La diferencia de lenguajes es {}".format(lenguajes)


desarrolladores = {
    1: {
        'nombre': 'Marco',
        'salario': 2500000,
        'habilidades': {
            'ingles': True,
            'lenguajes': {1: 'Ruby', 2: 'C#', 3: 'Basic', 4: 'Javascript', 5: 'PHP', 6: 'C++', 7: 'Python', 8: 'Fortran'},
            'entornos': 'VSC'
        }
    },
    2: {
        'nombre': 'Marco',
        'salario': 2500000,
        'habilidades': {
            'ingles': True,
            'lenguajes': {1: 'Python', 2: 'C#', 3: 'Java', 4: 'Javascript', 5: 'PHP', 6: 'Ruby', 7: 'C++'},
            'entornos': 'VSC'
        }
    }
}

cuentaLenguajes(desarrolladores)
diferenciaLenguajes(desarrolladores)
# print(diferencias(desarrolladores))
