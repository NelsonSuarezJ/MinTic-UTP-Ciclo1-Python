import json
import pandas as pd

dfData = pd.read_csv('data.csv')
# print(dfData)

data = ["Línea 1", "Línea 2", "Línea 3", "Línea 4", "Línea 5"]
fic = open("text_1.txt", "w", encoding="utf-8")

for line in data:
    fic.write(line)
    fic.write("\n")

fic.close()
print('----------------------------------------')
data = {}
data['clients'] = []

data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})

data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})

data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})

# escribe en el archivo
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
