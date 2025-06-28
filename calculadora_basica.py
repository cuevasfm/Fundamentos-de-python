from Fundamentos import nuevoTema
import Calc.operaciones as c

if __name__ == "__main__":
    nuevoTema("Modulos y paquetes")
    print(c.suma(1, 2, 3, 4, 5))
    print(c.resta(1, 2, 3, 4, 5))
    print(c.multiplicacion(1, 2, 3, 4, 5))
    print(c.division(10, 2))
