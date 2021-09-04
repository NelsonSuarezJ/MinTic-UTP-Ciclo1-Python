
def promedio_superior(p_nota):
    from functools import reduce
    try:
        p_nota = float(p_nota)
        students = {'a': {'name': 'Juan', 'notas': [3.1, 2.2, 2.5, 3.9, 3.2]},
                    'j': {'name': 'Jenny', 'notas': [2, 3.7, 2, 2, 2.2]},
                    'c': {'name': 'Ana', 'notas': [2.6, 2.7, 2.1, 2.9, 2.2]},
                    'y': {'name': 'Pedro', 'notas': [2, 3.5, 2, 2, 2.2]},
                    'x': {'name': 'Pablo', 'notas': [2, 3.3, 3.9, 3.2, 3.2]},
                    'l': {'name': 'Carlos', 'notas': [3.2, 3.8, 2.2, 2, 2.1]},
                    'v': {'name': 'Maria', 'notas': [2.8, 2.7, 2.8, 2.9, 2.8]},
                    'r': {'name': 'Luisa', 'notas': [2.8, 2.7, 3.5, 2.5, 2.9]},
                    'b': {'name': 'Mario', 'notas': [2.2, 3.2, 3, 4.2, 2.2]},
                    'g': {'name': 'Fabio', 'notas': [2.4, 3.2, 3.1, 3.2, 2.2]}}
        agruparNotas = [estudiante['notas'] for estudiante in students.values()]  # lista de listas de notas
        listaNotas = reduce(lambda x, y: x+y, agruparNotas)  # una sola lista con las notas
        listaNotasSuperior = list(filter(lambda numero: numero > p_nota, listaNotas))  # lista con solo notas superiores
        if listaNotasSuperior == []:
            return f'Ninguna nota supera {p_nota}'
        p_nota_total = round(sum(listaNotasSuperior)/len(listaNotasSuperior), 2)
        return f"{p_nota_total} es el promedio total"
    except:
        return "Error en el dato ingresado"


students = {'a': {'name': 'Juan', 'notas': [3.1, 2.2, 2.5, 3.9, 3.2]},
            'j': {'name': 'Jenny', 'notas': [2, 3.7, 2, 2, 2.2]},
            'c': {'name': 'Ana', 'notas': [2.6, 2.7, 2.1, 2.9, 2.2]},
            'y': {'name': 'Pedro', 'notas': [2, 3.5, 2, 2, 2.2]},
            'x': {'name': 'Pablo', 'notas': [2, 3.3, 3.9, 3.2, 3.2]},
            'l': {'name': 'Carlos', 'notas': [3.2, 3.8, 2.2, 2, 2.1]},
            'v': {'name': 'Maria', 'notas': [2.8, 2.7, 2.8, 2.9, 2.8]},
            'r': {'name': 'Luisa', 'notas': [2.8, 2.7, 3.5, 2.5, 2.9]},
            'b': {'name': 'Mario', 'notas': [2.2, 3.2, 3, 4.2, 2.2]},
            'g': {'name': 'Fabio', 'notas': [2.4, 3.2, 3.1, 3.2, 2.2]}}


print(promedio_superior(3))
print(promedio_superior('4'))
print(promedio_superior(5))
print(promedio_superior('Mundo'))
