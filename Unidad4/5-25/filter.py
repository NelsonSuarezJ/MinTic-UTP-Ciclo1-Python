# con filter (condicion falsa o true, lista)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mayores = list(filter(lambda i: i > 5, lista))
# print(mayores)

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

# filtrar con funcion filter
# filter_function = lambda dev: dev["salario"] > 2500000   (las lambda se convierte a def)


def filter_function(dev): return dev["salario"] > 2700000


filtered_list = list(filter(filter_function, devs))
print(filtered_list)

print('Con funcion anonima y funcion filter')
devsFilter = list(filter(lambda dev: dev['salario'] > 2500000, devs))
# print(devsFilter)
print("----------------------------------------------------------------")
# se puede crear una lista por comprehension que cumpla con la condicion sin necesidad de la funcion filter
print('Por comprehension:')
salarioDevs = [dev for dev in devs if dev["salario"] > 2500000]
# print(salarioDevs)
