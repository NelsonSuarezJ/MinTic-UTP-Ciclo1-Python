"""
Realizar una función que tome una lista y retorne un diccionario que contenga los valores de 
la lista como clave y el índice como el valor. Utilizar la función enumerate.
"""
paises = ['Colombia', 'Chile', 'Argentina', 'Brasil', 'Peru']
diccionario = {pais: indice for indice, pais in enumerate(paises)}
print(diccionario)
