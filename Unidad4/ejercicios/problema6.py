"""
Realizar una función que retorne el recuento de la cantidad de elementos en la lista cuyo 
valor es igual a su índice. Utilizar la función enumerate.
"""
numeros = [0, 1, 3, 6, 4, 3, 6]

cantidad = len([numero for indice, numero in enumerate(numeros) if indice == numero])
print(cantidad)
