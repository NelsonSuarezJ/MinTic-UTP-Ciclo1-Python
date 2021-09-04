import pandas as pd


def get_younger_users(age, url):
    try:
        age = int(age)
        diccionario = pd.read_json(url)
        lista = diccionario['results']
        listaMenores = list(filter(lambda edad: edad['dob']['age'] <= age, lista))
        respuesta = len(listaMenores)
        return respuesta
    except:
        return 0


print(get_younger_users('54', 'https://magicsolutions.co/users.json'))
