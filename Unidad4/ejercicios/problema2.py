"""
Crear una función que tome una lista de dígitos y devuelva al número al que corresponden. 
Por ejemplo [1,2,3] corresponde a el número ciento veintitrés (123). Utilizar la función 
reduce.
"""
from functools import reduce
numeros = [1, 2, 3, 4, 5, 6, 7]
concatenado = reduce(lambda a, b: str(a)+str(b), numeros)
print(concatenado)
