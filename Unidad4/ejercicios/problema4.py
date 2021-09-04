"""
Realizar una función que tome una lista de comprensión para devolver una lista de la misma 
longitud donde cada valor son las dos cadenas de L1 y L2 concatenadas con un conector entre 
ellas. Ejemplo: Listas: ['A', 'a'] ['B','b'] Conector: '-' Salida: ['A-a'] ['B-b']. Utilizar la función 
zip
"""


def concatenacion(L1, L2, connector):
    return [word1+connector+word2 for (word1, word2) in zip(L1, L2)]


print(concatenacion(['A', 'a'], ['B', 'b'], '-'))
