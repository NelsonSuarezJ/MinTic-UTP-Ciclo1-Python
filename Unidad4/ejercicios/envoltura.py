def crearFuncion(operador):
    if operador == "+":
        def suma(num1=0, num2=0):
            return num1 + num2
        return suma


def operacion(funcion, num1=0, num2=0):
    return funcion(num1, num2)


funcionSuma = crearFuncion('+')
resultado = operacion(funcionSuma, 10, 20)
print(resultado)
