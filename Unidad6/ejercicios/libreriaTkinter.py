from tkinter import *
from tkinter.ttk import *

app = Tk()

#print(Tcl().eval('info patchlevel'))
# app.iconbitmap("C:/Users/nelso/OneDrive/Apps/ProyectoVSCode/Ciclo1/Unidad6/ejercicios/python_original_logo.ico")
app.title("Primer ventana")
# app.geometry('800x300')
app.resizable(True, True)
# app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)

# Crear barra de menus, solo hay una en la app
barraMenus = Menu(app)
app.config(menu=barraMenus)

# se crea menu Archivo
menuArchivo = Menu(barraMenus, tearoff=0)
menuArchivo.add_command(label="Nuevo")
menuArchivo.add_command(label="Abrir...")
menuArchivo.add_command(label="Cerrar")
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir", command=app.destroy)
barraMenus.add_cascade(label="Archivo", menu=menuArchivo, underline=0)  # adiciona items al menu Archivo

# se crea menu Ayuda
menuAyuda = Menu(barraMenus, tearoff=0)
menuAyuda.add_command(label='Buscar actualizaciones')
menuAyuda.add_command(label='Acerca de...')
barraMenus.add_cascade(label="Ayuda", menu=menuAyuda, underline=1)  # adiciona items al menu Ayuda

etiquetaNombre = Label(app, text='Nombre: ')
etiquetaNombre.grid(row=0, column=0, sticky=W, padx=5, pady=5)

textoNombre = Entry(app)
textoNombre.grid(row=0, column=1, sticky=W+E, padx=5)

cajaTexto = Text(app)
cajaTexto.grid(row=1, column=0, columnspan=2, sticky='EWSN', padx=5)

botonGuardar = Button(app, text='Guardar')
botonGuardar.grid(row=2, column=1, sticky=E, padx=5, pady=5, ipady=5)


# al final
app.mainloop()
