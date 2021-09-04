frutas = {'fresa': 'roja', 'naranja': 'anaranjada', 'manzana': 'verde', 'banano': 'amarillo', 'limon': 'verde'}

""" for nombre, color in frutas.items():
    print(nombre, "=", color)

for f in frutas:  # muestra las claves
    print(f)

for g in frutas:  # muestra los valores
    print(frutas[g])

for h in frutas.values():  # muestra los valores
    print(h)
"""

# filtra un diccionario por frutas verdes
frutasVerdes = list(filter(lambda fruta: fruta[1] == 'verde', frutas.items()))
print(frutasVerdes)
