texto = "mucho texto"
lista = list(texto)  # de string a lista
print(texto)
print(lista)

aString = ''.join(lista)  # de lista a string
print(aString)

tupla = tuple(lista)  # de lista a tuplan
print(tupla)

diccionario = {'nombre': 'nelson', 'apellido': 'suarez', 'edad': 39}
claves = list(diccionario)  # de diccionario a lista de claves
print('lista=', claves)

diccATupla = tuple(diccionario)  # de diccionario a tupla de claves
print('tupla=', diccATupla)
