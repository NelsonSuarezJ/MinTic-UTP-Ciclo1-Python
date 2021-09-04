# lista con numeros del 1 al 9
lista = [i for i in range(1, 10)]
# print(lista)

# lista con los numeros impares del 1 al 10
lista1 = [i for i in range(1, 10) if i % 2 == 1]
# print(lista1)

# lista con multiplos de 4 y 5
multiplo4y5 = [n for n in range(1, 5000) if n % 4 == 0 and n % 5 == 0]
# print(multiplo4y5)

# lista con los elementos que estan en lista2 pero no en pares
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [2, 4, 6, 8, 10]
noEnPares = [n for n in lista2 if n not in pares]
# print(noEnPares)

devs = [
    {"cc": 1540, "nombre": "Miguel", "salario": 2600000, "years": 5},
    {"cc": 1556, "nombre": "Cristian", "salario": 2500000, "years": 2},
    {"cc": 2556, "nombre": "Juan Ignacio", "salario": 2500000, "years": 3},
    {"cc": 1340, "nombre": "Nicolas", "salario": 2400000, "years": 4},
    {"cc": 1526, "nombre": "Sendy", "salario": 2400000, "years": 5},
    {"cc": 2516, "nombre": "Santiago", "salario": 2600000, "years": 5},
    {"cc": 1547, "nombre": "David", "salario": 2500000, "years": 3},
    {"cc": 5556, "nombre": "Milton", "salario": 2800000, "years": 6},
    {"cc": 5586, "nombre": "Jinneth", "salario": 2800000, "years": 2},
    {"cc": 3556, "nombre": "Alejandro", "salario": 2700000, "years": 1},
]


listaDevs = [dev for dev in devs if dev["salario"] > 2500000]
# print(listaDevs)
