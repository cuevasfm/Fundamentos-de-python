from tkinter import *
from tkinter import ttk


raiz = Tk()
raiz.title("Inicio de sesion")
raiz.geometry("370x200")

marcoPrincipal = ttk.Frame(raiz, padding="3 3 12 12")
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))
marcoPrincipal.columnconfigure(0, weight=1)
marcoPrincipal.rowconfigure(0, weight=1)




usuario = StringVar()
contrasena = StringVar()

ttk.Label(marcoPrincipal, text="Inicio de sesion", font=("Arial", 18, "bold")).grid(column=0, row=0, columnspan=3, sticky=N, pady=10, padx=10)

ttk.Label(marcoPrincipal, text="Usuario:").grid(column=0, row=1, sticky=E)
ttk.Label(marcoPrincipal, text="Contraseña:").grid(column=0, row=2, sticky=E)

txtUsuario = ttk.Entry(marcoPrincipal, width=30, textvariable=usuario)
txtUsuario.grid(column=1, row=1, columnspan=2, sticky=(W, E), pady=10, padx=4)

txtContrasena = ttk.Entry(marcoPrincipal, width=30, textvariable=contrasena)
txtContrasena.grid(column=1, row=2, columnspan=2, sticky=(W, E), pady=10, padx=4)

ttk.Button(marcoPrincipal, text="Iniciar sesion").grid(column=2, row=3, sticky=E, pady=10, padx=4)

raiz.mainloop()




