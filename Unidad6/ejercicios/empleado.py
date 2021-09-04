class Empleado():
    def __init__(self):
        self.nombre = input("Ingrese nombre: ")
        self.sueldo = int(input("Ingrese el sueldo: "))

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Sueldo: {self.sueldo}")

    def impuesto(self):
        if self.sueldo > 3000:
            print('Debe pagar impuesto')
        else:
            print('No debe pagar impuesto')


empleado1 = Empleado()
empleado1.imprimir()
empleado1.impuesto()
empleado1.nombre = 'juan'
empleado1.imprimir()
