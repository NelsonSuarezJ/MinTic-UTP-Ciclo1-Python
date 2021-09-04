"""
Crear una función que retorne las palabras de una lista de palabras que comience con una 
letra en específico. Utilizar la función filter.
"""
paises = ['Colombia', 'Peru', 'Costa Rica', 'Venezuela', 'Paraguay', 'Bolivia']
paisesLetra = list(filter(lambda pais: pais.startswith('C'), paises))
print(paisesLetra)
