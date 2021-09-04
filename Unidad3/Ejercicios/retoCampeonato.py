def dar_mejor_y_peor_competidor(competidores):
    if isinstance(competidores, dict) and competidores != {}:
        mejor = 10
        promedioPerdedor = 0
        for competidor in competidores.values():
            promedio = round(sum(competidor['tiempos'])/len(competidor['tiempos']), 2)
            if promedio <= mejor:
                mejor = promedio
                ganador = competidor['name']
            if promedio >= promedioPerdedor:
                promedioPerdedor = promedio
                ultimo = competidor['name']
        return f"El ganador es {ganador} con un tiempo promedio de {mejor}. El premio de consolación es para {ultimo}"
    else:
        return "El formato del diccionario no es válido"


diccionario = {0: {'name': 'Camilo', 'tiempos': [3.12, 3.2, 3.3, 3.21]},
               1: {'name': 'Ana', 'tiempos': [3.21, 3.17, 3.15, 3.19]}}

diccionario2 = {0: {'name': 'Camilo', 'tiempos': [3.12, 3.2, 3.1, 3.21]},
                1: {'name': 'Ana', 'tiempos': [3.21, 3.27, 3.15, 3.19]},
                2: {'name': 'Carlos', 'tiempos': [3.3, 3.27, 3.24, 3.19]},
                3: {'name': 'Pedro', 'tiempos': [3.3, 3.3, 3.4, 3.25]},
                4: {'name': 'Fabio', 'tiempos': [3.4, 3.28, 3.29, 3.24]}}

diccionario3 = {0: {'name': 'Camilo', 'tiempos': [3.12, 3.2, 3.3, 3.21]},
                1: {'name': 'Ana', 'tiempos': [3.51, 3.17, 3.15, 3.19]},
                2: {'name': 'Carlos', 'tiempos': [3.3, 3.27, 3.24, 3.19]},
                3: {'name': 'Pedro', 'tiempos': [3.3, 3.3, 3.4, 3.25]},
                4: {'name': 'Fabio', 'tiempos': [3.4, 3.28, 3.29, 3.24]},
                5: {'name': 'Maria', 'tiempos': [3.24, 3.14, 3.26, 3.19]},
                6: {'name': 'Laura', 'tiempos': [3.8, 3.7, 3.5, 3.5]}}

diccionario4 = {0: {'name': 'Camilo', 'tiempos': [3.12, 3.2, 3.1, 3.21]},
                1: {'name': 'Ana', 'tiempos': [3.21, 3.27, 3.15, 3.19]},
                2: {'name': 'Carlos', 'tiempos': [3.12, 3.2, 3.1, 3.21]},
                3: {'name': 'Pedro', 'tiempos': [3.3, 3.3, 3.4, 3.25]},
                4: {'name': 'Fabio', 'tiempos': [3.4, 3.28, 3.29, 3.24]}}

dicc = {}
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# dar_mejor_y_peor_competidor(diccionario3)
print(dar_mejor_y_peor_competidor(diccionario))
print(dar_mejor_y_peor_competidor(diccionario2))
print(dar_mejor_y_peor_competidor(diccionario3))
print(dar_mejor_y_peor_competidor(dicc))
