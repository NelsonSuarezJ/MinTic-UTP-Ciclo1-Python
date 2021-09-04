desarrollador = {
    'nombre': 'Nelson',
    'salario': 2500000,
    'habilidades': {
        'ingles': True,
        'lenguajes': {
            1: 'Python',
            2: 'C#',
            3: 'Java',
            4: 'Javascript',
            5: 'PHP'
        },
        'entornos': 'VSC'
    }
}


def mostrarInfo(desarrollador):
    if len(desarrollador['habilidades']['lenguajes']) >= 5:
        return "Sabe 5 lenguajes"
    else:
        return "Sabe menos de 5 lenguajes"


print(mostrarInfo(desarrollador))
