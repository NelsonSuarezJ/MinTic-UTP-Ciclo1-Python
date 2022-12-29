"""funcion que calcula la cantidad de trozos y tiempo que se demora en cortarlos"""


def calcular_trozos(rollos):
    """Calcula la cantidad de trozos por minuto"""
    trozos = rollos*10
    tiempo_carga = 3
    tiempo_corte = 2
    minutos = (tiempo_carga+tiempo_corte)*cantidad_rollos
    return  f"La máquina arrojó {trozos} trozos de tela en {minutos} minutos."


cantidad_rollos = int(
    input("Ingrese la cantidad de rollos de tela a cortar: "))
respuesta = calcular_trozos(cantidad_rollos)
print(respuesta)
