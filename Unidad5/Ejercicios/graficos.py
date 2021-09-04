import matplotlib.pyplot as plt

x1 = [2, 5, 6, 14]
y1 = [11, 22, 33, 44]

x2 = [2, 5, 6, 15]
y2 = [4, 12, 18, 45]


def construirGrafica(titulo):
    plt.title(titulo)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.grid()
    plt.show()


# plt.plot(x1, y1, color='blue', linewidth=3, label='Linea 1')
# plt.plot(x2, y2, color='red', linewidth=3, label='Linea 2')
#construirGrafica('Dos lineas en un grafico')


# plt.bar(x1, y1, color='blue', label='Barra 1')
# plt.bar(x2, y2, color='red', label='Barra 2')
# construirGrafica('Grafico de barras')

# plt.scatter(x1, y1, color="red",  label='Puntos 1')
# construirGrafica('Grafico de puntos')

valores = [20, 40, 60, 80]
plt.pie(valores, labels=['Prekinder', 'kinder', 'primaria', 'secundaria'], colors=[
        'red', 'purple', 'blue', 'orange'], startangle=90, shadow=True, explode=(0.1, 0, 0, 0), autopct='%1.1f%%')
plt.title('Grafico circular')
plt.show()
