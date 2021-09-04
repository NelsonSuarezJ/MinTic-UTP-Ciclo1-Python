import pandas as pd
import matplotlib.pyplot as plt

dfTitanic = pd.read_csv('titanic3.csv')
# print(dfTitanic)

# plt.figure(figsize=(30, 20))

# for class_i in [1, 2, 3]:
#     dfTitanic.age[dfTitanic.pclass == class_i].plot(kind='kde')

# plt.show()
# ----------------------------------------------------------------
datos = {'name': ['john', 'mary', 'peter', 'jeff', 'bill', 'lisa', 'jose'],
         'age': [23, 78, 22, 19, 45, 33, 20],
         'gender': ['M', 'F', 'M', 'M', 'M', 'F', 'M'],
         'state': ['california', 'dc', 'california', 'dc', 'california', 'texas', 'texas'],
         'num_children': [2, 0, 0, 3, 2, 1, 4],
         'num_pets': [5, 1, 0, 5, 2, 2, 3]}

df = pd.DataFrame(datos)
print(df)
df.plot(kind='bar', x='name', y='age', color='blue')
plt.show()
