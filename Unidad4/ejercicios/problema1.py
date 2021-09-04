"""
Utilizar la función incorporada map() para crear una función que retorne una lista con la 
longitud de cada palabra (separadas por espacios) de una frase. La función recibe una cadena 
de texto y retornará una lista.
"""
frase = "Hoy es miercoles dos de junio"
#longitudPalabras = list(map(lambda palabra: len(palabra), frase.split()))
longitudPalabras = list(map(len, frase.split()))
print(longitudPalabras)


def longitud_palabras(frase):  # Función
    palabra_len = list(map(len, frase.split()))  # Longitud de cada palabra
    return palabra_len  # Retornar resultado


print(longitud_palabras('Hola Luis, como estas?'))  # Prueba de la función
