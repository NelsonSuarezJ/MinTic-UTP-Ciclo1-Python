# pip install pandas, para instalar la libreria
import pandas as pd

serie1 = pd.Series([5, 7, 3])
serie11 = pd.Series([1, 2, 3], index=['Ene', 'Feb', 'Mar'])
serie11.name = 'Festivos por mes'
serie11.index.name = 'Meses'

serie2 = pd.Series({'dia1': 1, 'dia2': 2, 'dia3': 3})
frame1 = pd.DataFrame({'dia1': [2, 3, 4], 'dia2': [5, 6, 7], 'dia3': [8, 9, 1]})
frame2 = pd.DataFrame([[2, 3, 4], [5, 6, 7], [8, 9, 1]], columns=['dia1', 'dia2', 'dia3'])

# print(serie1)
# print(serie11)
datos = {'manzanas': [3, 2, 0, 1], 'naranjas': [0, 3, 7, 2]}
compras = pd.DataFrame(datos, index=['Juno', 'Robert', 'Lily', 'David'])
compras.index.name = 'Clientes'
compras.columns.name = 'Frutas'

data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
dataframeData = pd.DataFrame(data)
print(dataframeData)
print(pd.DataFrame.from_dict(data))
