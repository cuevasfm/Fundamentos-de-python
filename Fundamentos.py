def nuevoTema(_tema: str):
    print(f"\n------{_tema}------\n")

'''
Operadores aritméticos
1HAcer tablas de verdad
2Ejemplo de cada operador de comparación
'''
if __name__ == "__main__":
    nuevoTema("Operadores aritméticos")
    print("Operador suma 5 + 6 = ", 5 + 6) # Suma 5 y 6
    print("Operador resta 5 - 6 = ", 5 - 6) # Resta 5 y 6
    print("Operador multiplicación 5 * 6 = ", 5 * 6) # Multiplica 5 por 6
    print("Operador división 5 / 6 = ", 5 / 6) # Divide 5 por 6
    print("Operador módulo 5 % 6 = ", 5 % 6) # Devuelve el resto de la división
    print("Operador potencia 5 ** 6 = ", 5 ** 6) # 5 elevado a 6
    print("Operador división entera 5 // 6 = ", 5 // 6) # División entera, devuelve el cociente de la división
    print("Operador de cambio de signo -5 = ", -5)  # Cambia el signo de 5 a -5
    print("-----------------------------------")

    nuevoTema("Operadores lógicos")
    print("Operador and")
    print("Operador and True and True = ", True and True) # Devuelve True si ambas expresiones son True, False en caso contrario
    print("Operador and True and False = ", True and False) # Devuelve True si ambas expresiones son True, False en caso contrario
    print("Operador and False and True = ", False and True) # Devuelve True si ambas expresiones son True, False en caso contrario
    print("Operador and False and False = ", False and False) # Devuelve True si ambas expresiones son True, False en caso contrario
    print("-----------------------------------")
    print("Operador or")
    print("Operador or True or True = ", True or True) # Devuelve True si alguna de las expresiones es True, False en caso contrario
    print("Operador or True or False = ", True or False) # Devuelve True si alguna de las expresiones es True, False en caso contrario
    print("Operador or False or True = ", False or True) # Devuelve True si alguna de las expresiones es True, False en caso contrario
    print("Operador or False or False = ", False or False) # Devuelve True si alguna de las expresiones es True, False en caso contrario
    print("Operador not True = ", not True) # Devuelve True si la expresión es False, False en caso contrario
    print("-----------------------------------")

    nuevoTema("Operadores de comparación")
    print("Operador igual que 5 == 6 = ", 5 == 6) # Devuelve True si 5 es igual a 6, False en caso contrario
    print("Operador diferente que 5 != 6 = ", 5 != 6) # Devuelve True si 5 es diferente a 6, False en caso contrario
    print("Operador mayor que 5 > 6 = ", 5 > 6) # Devuelve True si 5 es mayor que 6, False en caso contrario
    print("Operador menor que 5 < 6 = ", 5 < 6) # Devuelve True si 5 es menor que 6, False en caso contrario
    print("Operador mayor o igual que 5 >= 6 = ", 5 >= 6) # Devuelve True si 5 es mayor o igual que 6, False en caso contrario
    print("Operador menor o igual que 5 <= 6 = ", 5 <= 6) # Devuelve True si 5 es menor o igual que 6, False en caso contrario
    print("-----------------------------------")

    nuevoTema("Operadores de asignación")
    x = 5
    print("Operador de asignación = : x = 5 da", x) # Asigna el valor 5 a x
    x += 6  
    print("Operador de asignación += : x += 6 da", x) # Suma 6 a x y guarda resultado en x
    x -= 6
    print("Operador de asignación -= : x -= 6 da", x) # Resta 6 a x y guarda resultado en x
    print("-----------------------------------")

    variable = 1.123456789012345678
    print(variable)
    print(type(variable))

    nuevoTema("Enteros")
    x = 10
    print(x)
    print(type(x))

    nuevoTema("Binarios")
    x = 0b1010
    print(x)
    print(type(x))

    nuevoTema("Hexadecimales")
    x = 0xF1
    print(x)
    print(type(x))

    nuevoTema("Flotantes")
    x = 10.0
    print(x)
    print(type(x))

    nuevoTema("Complejos")
    x = 10 + 5j
    print(x)
    print(type(x))

    nuevoTema("Cadenas de texto")
    x = "Hola"
    print(x)
    print(type(x))

    nuevoTema("Booleanos")
    x = True
    y = False
    print(x)
    print(type(x))
    print(y)
    print(type(y))

    nuevoTema("Listas")
    x = [1, 2, 3, 4, 5]
    x
    print(x)
    print(type(x))
    x.append(7)
    print(x)
    print(type(x))
    x.insert(5, 6)
    print(x)
    print(type(x))
    x.pop()
    print(x)
    print(type(x))
    x.clear()
    print(x)
    print(type(x))
    x.append([6, 7, 8])
    print(x)
    print(type(x))
    x.extend([9, 10, 11])
    print(x)
    print(type(x))
    x.remove([6, 7, 8])

    nuevoTema("Tuplas")
    x = (1, 2, 3, 4, 5)
    print(x)
    print(type(x))
    x = (1, 2, 3, 4, 5, 7)
    print(x)
    print(type(x))

    nuevoTema("Diccionarios")
    x = {
        "nombre": "Juan", 
        "edad": 20,
        "ciudad": "Guadalajara",
        "objetos": ["laptop", "celular", "tablet"],
        "direccion": {
            "calle": "Av. Revolución",
            "numero": 123,
            "colonia": "Centro",
            "cp": 44100
        }
    }
    print(x)
    print(type(x))  
    print(x["nombre"])
    print(x["edad"])
    print(x["ciudad"])
    print(x["objetos"])
    print(x["direccion"])
    print(x["direccion"]["calle"])
    print(x["direccion"]["numero"])
    print(x["direccion"]["colonia"])
    print(x["direccion"]["cp"])

    nuevoTema("Sets")
    x = {1, 2, 3, 4, 5}
    y = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    print(x)
    print(type(x))

    #Buscar elemento set
    print("1 esta en x: ", 1 in x)
    #operaciones con sets
    print("Union de sets: ", x.union(y))
    print("Intersección de sets: ", x.intersection(y))
    print("Diferencia de sets: ", x.difference(y))
    print("Diferencia simétrica de sets: ", x.symmetric_difference(y))
    print("x es subconjunto de y: ", x.issubset(y))
    print("x es superconjunto de y: ", x.issuperset(y))

    nuevoTema("None")
    x = None
    print(x)
    print(type(x))

    nuevoTema("Cadenas")
    x = "Hola esto es una cadena de texto"
    print(x)
    print(type(x))
    print(x[0])
    print(x[1])
    print(x[2])
    print(x[3])
    #imprimir al reves
    print(x[::-1])
    #imprimir desde el 5 al 10
    print(x[5:10])
    #imprimir desde el 5 al 10 de 2 en 2
    print(x[5:15:2])
    #imprimir desde el 5 al 10 de 2 en 2
    print(x[5:10:3])