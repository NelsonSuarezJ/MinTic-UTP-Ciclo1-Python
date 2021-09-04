import pandas as pd

devs = [{'cc': 1540, 'nombre': 'Miguel', 'salario': 2600000, 'years': 5},
        {'cc': 1556, 'nombre': 'Cristian', 'salario': 2500000, 'years': 2},
        {'cc': 2556, 'nombre': 'Juan Ignacio', 'salario': 2500000, 'years': 3},
        {'cc': 1340, 'nombre': 'Nicolas', 'salario': 2400000, 'years': 4},
        {'cc': 1526, 'nombre': 'Sendy', 'salario': 2400000, 'years': 5},
        {'cc': 2516, 'nombre': 'Santiago', 'salario': 2600000, 'years': 5},
        {'cc': 1547, 'nombre': 'David', 'salario': 2500000, 'years': 3},
        {'cc': 5556, 'nombre': 'Milton', 'salario': 2800000, 'years': 6},
        {'cc': 5586, 'nombre': 'Jinneth', 'salario': 2800000, 'years': 2},
        {'cc': 3556, 'nombre': 'Alejandro', 'salario': 2700000, 'years': 1}]

devs2 = [{'cc': 1540, 'nombre': 'Miguel', 'salario': 2600000, 'years': 5, 'langs': {0: 'Python', 1: 'Javascript'}},
         {'cc': 1556, 'nombre': 'Cristian', 'salario': 2500000, 'years': 2, 'langs': {0: 'xx', 1: 'Javascript'}},
         {'cc': 2556, 'nombre': 'Juan Ignacio', 'salario': 2500000, 'years': 3, 'langs': {0: 'Python', 1: 'Javascript'}},
         {'cc': 1340, 'nombre': 'Nicolas', 'salario': 2400000, 'years': 4, 'langs': {0: 'xx', 1: 'Javascript'}},
         {'cc': 1526, 'nombre': 'Sendy', 'salario': 2400000, 'years': 5, 'langs': {0: 'Python', 1: 'Javascript'}},
         {'cc': 2516, 'nombre': 'Santiago', 'salario': 2600000, 'years': 5, 'langs': {0: 'xx', 1: 'Javascript'}},
         {'cc': 1547, 'nombre': 'David', 'salario': 2500000, 'years': 3, 'langs': {0: 'Python', 1: 'Javascript'}},
         {'cc': 5556, 'nombre': 'Milton', 'salario': 2800000, 'years': 6, 'langs': {0: 'xx', 1: 'Javascript'}},
         {'cc': 5586, 'nombre': 'Jinneth', 'salario': 2800000, 'years': 2, 'langs': {0: 'Python', 1: 'Javascript'}},
         {'cc': 3556, 'nombre': 'Alejandro', 'salario': 2700000, 'years': 1, 'langs': {0: 'xx', 1: 'Javascript'}}]
# crea un datafreme de las lista devs
devsPanda = pd.DataFrame(devs)
# print(devsPanda)

# le asigna indices con cedulas para poder buscar mas facil las filas
devs2Panda = pd.DataFrame(devs, index=[dev['cc'] for dev in devs])
# print(devs2Panda)

# le paso el numero de indice para que me traiga los datos
# print(devs2Panda.loc[2556])

# -------------------------------------
devsPanda = pd.DataFrame(devs)
devsPanda.to_csv('devsEncsv.csv', index=False)
devsPanda.to_json('devsEnJson.json')
# -------------------------------------
leerDevs = pd.read_csv('devsEncsv.csv')
#leerDevs = pd.read_json('devsEnJson.json')
# print(leerDevs)

#print(leerDevs.loc[lambda elemento: elemento['salario'] <= 2500000])
# -------------------
# forma 1 de almacenar solo columna 'langs', queda como dataframe
devs2Panda = pd.DataFrame(dev['langs'] for dev in devs2)
devs2p = pd.DataFrame(devs2)
devs2pLangs = devs2p.get('langs')  # forma 2 de almacenar solo columna 'langs', queda como Serie
print(devs2Panda)
print(devs2pLangs)
#print(devs2Panda[devs2Panda[0] == 'Python'])

# print(devs2Panda.loc[lambda elemento: elemento[0] == 'Python'])
