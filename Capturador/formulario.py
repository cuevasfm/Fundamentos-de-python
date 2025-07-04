from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import os
from datetime import datetime


class Persona:
    
    def __init__(self, nombre="", apellido_paterno="", apellido_materno="", 
                 correo="", movil="", estado_civil="Estudiante", 
                 leer=False, musica=False, videojuegos=False, estado=""):
        self.nombre = nombre 
        self.apellido_paterno = apellido_paterno 
        self.apellido_materno = apellido_materno
        self.correo = correo
        self.movil = movil
        self.estado_civil = estado_civil
        self.leer = leer
        self.musica = musica
        self.videojuegos = videojuegos
        self.estado = estado
        self.fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
    
    def validar_datos(self):
        campos_obligatorios = [
            (self.nombre, "Nombre"),
            (self.apellido_paterno, "Apellido Paterno"),
            (self.correo, "Correo")
        ]
        
        campos_vacios = [campo[1] for campo in campos_obligatorios if not campo[0].strip()]
        
        if campos_vacios:
            return False, f"Por favor complete los campos obligatorios: {', '.join(campos_vacios)}"
        
        if "@" not in self.correo or "." not in self.correo:
            return False, "Por favor ingrese un correo válido"
        
        return True, "Datos válidos"
    
    def obtener_nombre_completo(self):
        nombres = [self.nombre, self.apellido_paterno, self.apellido_materno]
        return " ".join([n for n in nombres if n.strip()])
    
    def obtener_aficiones(self):
        aficiones = []
        if self.leer:
            aficiones.append("Leer")
        if self.musica:
            aficiones.append("Música")
        if self.videojuegos:
            aficiones.append("Videojuegos")
        return aficiones
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'apellido_paterno': self.apellido_paterno,
            'apellido_materno': self.apellido_materno,
            'correo': self.correo,
            'movil': self.movil,
            'estado_civil': self.estado_civil,
            'leer': self.leer,
            'musica': self.musica,
            'videojuegos': self.videojuegos,
            'estado': self.estado,
            'fecha_registro': self.fecha_registro
        }
    
    @classmethod
    def from_dict(cls, datos):
        return cls(
            nombre=datos.get('nombre', ''),
            apellido_paterno=datos.get('apellido_paterno', ''),
            apellido_materno=datos.get('apellido_materno', ''),
            correo=datos.get('correo', ''),
            movil=datos.get('movil', ''),
            estado_civil=datos.get('estado_civil', 'Estudiante'),
            leer=datos.get('leer', False),
            musica=datos.get('musica', False),
            videojuegos=datos.get('videojuegos', False),
            estado=datos.get('estado', '')
        )


class FormularioApp:
    
    def __init__(self):
        self.raiz = Tk()
        self.archivo_csv = './datos_formulario.csv'
        self.persona_actual = Persona()
        
        self.estados_mexico = [
            "Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Ciudad de México",
            "Chiapas", "Chihuahua", "Coahuila", "Colima", "Durango", "Estado de México", "Guanajuato",
            "Guerrero", "Hidalgo", "Jalisco", "Michoacán", "Morelos", "Nayarit", "Nuevo León",
            "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa",
            "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"
        ]
        
        self.configurar_ventana()
        self.crear_variables()
        self.crear_interfaz()
        self.configurar_layout()
    
    def configurar_ventana(self):
        self.raiz.title("Muestra Widgets - Gestión de Personas")
        self.raiz.geometry("750x550")
        self.raiz.resizable(True, True)
    
    def crear_variables(self):
        self.nombre = StringVar()
        self.apellido_paterno = StringVar()
        self.apellido_materno = StringVar()
        self.correo = StringVar()
        self.movil = StringVar()
        self.estado_civil = StringVar()
        self.estado_civil.set('Estudiante')
        self.leer_var = BooleanVar()
        self.musica_var = BooleanVar()
        self.videojuegos_var = BooleanVar()
        self.estado_seleccionado = StringVar()
    
    def crear_interfaz(self):
        self.marco_principal = ttk.Frame(self.raiz, padding="10 10 10 10")
        self.marco_principal.grid(column=0, row=0, sticky=(N, W, E, S))
        
        ttk.Label(self.marco_principal, text="Gestión de Personas", 
                  font=("Arial", 16, "bold")).grid(column=0, row=0, columnspan=4, pady=10)
        
        self.crear_seccion_datos_personales()
        self.crear_seccion_estado()
        self.crear_seccion_aficiones()
        self.crear_seccion_ubicacion()
        self.crear_botones()
    
    def crear_seccion_datos_personales(self):
        self.marco_datos = ttk.LabelFrame(self.marco_principal, text="Datos Personales", padding="10 10 10 10")
        self.marco_datos.grid(column=0, row=1, columnspan=2, sticky=(W, E), pady=10)
        
        ttk.Label(self.marco_datos, text="Nombre:").grid(column=0, row=0, sticky=W, pady=5)
        self.entrada_nombre = ttk.Entry(self.marco_datos, textvariable=self.nombre, width=30)
        self.entrada_nombre.grid(column=1, row=0, sticky=(W, E), padx=5, pady=5)
        
        ttk.Label(self.marco_datos, text="A. Paterno:").grid(column=0, row=1, sticky=W, pady=5)
        ttk.Entry(self.marco_datos, textvariable=self.apellido_paterno, width=30).grid(column=1, row=1, sticky=(W, E), padx=5, pady=5)
        
        ttk.Label(self.marco_datos, text="A. Materno:").grid(column=0, row=2, sticky=W, pady=5)
        ttk.Entry(self.marco_datos, textvariable=self.apellido_materno, width=30).grid(column=1, row=2, sticky=(W, E), padx=5, pady=5)
        
        ttk.Label(self.marco_datos, text="Correo:").grid(column=0, row=3, sticky=W, pady=5)
        ttk.Entry(self.marco_datos, textvariable=self.correo, width=30).grid(column=1, row=3, sticky=(W, E), padx=5, pady=5)
        
        ttk.Label(self.marco_datos, text="Móvil:").grid(column=0, row=4, sticky=W, pady=5)
        ttk.Entry(self.marco_datos, textvariable=self.movil, width=30).grid(column=1, row=4, sticky=(W, E), padx=5, pady=5)
    
    def crear_seccion_estado(self):
        self.marco_estado = ttk.LabelFrame(self.marco_principal, text="Estado Civil", padding="10 10 10 10")
        self.marco_estado.grid(column=2, row=1, sticky=(N, W, E, S), padx=(10, 0), pady=10)
        
        ttk.Radiobutton(self.marco_estado, text="Estudiante", variable=self.estado_civil, 
                        value="Estudiante").grid(column=0, row=0, sticky=W, pady=2)
        ttk.Radiobutton(self.marco_estado, text="Empleado", variable=self.estado_civil, 
                        value="Empleado").grid(column=0, row=1, sticky=W, pady=2)
        ttk.Radiobutton(self.marco_estado, text="Desempleado", variable=self.estado_civil, 
                        value="Desempleado").grid(column=0, row=2, sticky=W, pady=2)
    
    def crear_seccion_aficiones(self):
        self.marco_aficiones = ttk.LabelFrame(self.marco_principal, text="Aficiones", padding="10 10 10 10")
        self.marco_aficiones.grid(column=0, row=2, columnspan=2, sticky=(W, E), pady=10)
        
        ttk.Checkbutton(self.marco_aficiones, text="Leer", variable=self.leer_var).grid(column=0, row=0, sticky=W, padx=5)
        ttk.Checkbutton(self.marco_aficiones, text="Música", variable=self.musica_var).grid(column=1, row=0, sticky=W, padx=5)
        ttk.Checkbutton(self.marco_aficiones, text="Videojuegos", variable=self.videojuegos_var).grid(column=2, row=0, sticky=W, padx=5)
    
    def crear_seccion_ubicacion(self):
        self.marco_ubicacion = ttk.LabelFrame(self.marco_principal, text="Ubicación", padding="10 10 10 10")
        self.marco_ubicacion.grid(column=2, row=2, sticky=(N, W, E, S), padx=(10, 0), pady=10)
        
        ttk.Label(self.marco_ubicacion, text="Estados:").grid(column=0, row=0, sticky=W, pady=5)
        
        self.combo_estados = ttk.Combobox(self.marco_ubicacion, textvariable=self.estado_seleccionado, 
                                         values=self.estados_mexico, width=25, state="readonly")
        self.combo_estados.grid(column=0, row=1, sticky=(W, E), pady=5)
    
    def crear_botones(self):
        self.marco_botones = ttk.Frame(self.marco_principal, padding="10 10 10 10")
        self.marco_botones.grid(column=0, row=3, columnspan=4, pady=20)
        
        ttk.Button(self.marco_botones, text="Guardar", command=self.guardar_persona).grid(column=0, row=0, padx=10)
        ttk.Button(self.marco_botones, text="Cancelar", command=self.cancelar).grid(column=1, row=0, padx=10)
    
    def configurar_layout(self):
        self.raiz.columnconfigure(0, weight=1)
        self.raiz.rowconfigure(0, weight=1)
        
        self.marco_principal.columnconfigure(0, weight=2)
        self.marco_principal.columnconfigure(1, weight=1)
        self.marco_principal.columnconfigure(2, weight=1)
        self.marco_datos.columnconfigure(1, weight=1)
        self.marco_ubicacion.columnconfigure(0, weight=1)
        
        self.raiz.after(100, lambda: self.entrada_nombre.focus())
    
    def obtener_datos_formulario(self):
        return Persona(
            nombre=self.nombre.get().strip(),
            apellido_paterno=self.apellido_paterno.get().strip(),
            apellido_materno=self.apellido_materno.get().strip(),
            correo=self.correo.get().strip(),
            movil=self.movil.get().strip(),
            estado_civil=self.estado_civil.get(),
            leer=self.leer_var.get(),
            musica=self.musica_var.get(),
            videojuegos=self.videojuegos_var.get(),
            estado=self.estado_seleccionado.get()
        )
    
    def guardar_persona(self):
        try:
            persona = self.obtener_datos_formulario()
            
            es_valido, mensaje = persona.validar_datos()
            if not es_valido:
                messagebox.showerror("Error de Validación", mensaje)
                return
            
            archivo_existe = os.path.exists(self.archivo_csv)
            
            with open(self.archivo_csv, 'a', newline='', encoding='utf-8') as archivo:
                campos = ['nombre', 'apellido_paterno', 'apellido_materno', 'correo', 'movil', 
                         'estado_civil', 'leer', 'musica', 'videojuegos', 'estado', 'fecha_registro']
                escritor = csv.DictWriter(archivo, fieldnames=campos)
                
                if not archivo_existe:
                    escritor.writeheader()
                
                escritor.writerow(persona.to_dict())
            
            messagebox.showinfo("Éxito", 
                              f"Persona '{persona.obtener_nombre_completo()}' guardada correctamente en {self.archivo_csv}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar los datos: {str(e)}")
    
    def cancelar(self):
        respuesta = messagebox.askyesno("Confirmar", "¿Está seguro que desea salir de la aplicación?")
        if respuesta:
            self.raiz.destroy()
    
    def ejecutar(self):
        self.raiz.mainloop()

if __name__ == "__main__":
    app = FormularioApp()
    app.ejecutar() 