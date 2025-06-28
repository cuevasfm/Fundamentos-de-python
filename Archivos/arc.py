file = open("EjemplArchivo.txt", "w")
file.write("Este es el contenido del archivo editado")
file.close()


lista = ["Fresa", "Mango", "Pera", "Uva"]

with open("EjemplArchivo.txt", "a") as file:
    file.write("\nNombres de frutas:\n")
    for item in lista:
        file.write(item + "\n")

print("Lista escrita en el archivo")

lista2 = ["honda", "yamaha", "suzuki", "kawasaki"]

with open("EjemplArchivo.txt", "a") as file:
    file.write("\nNombres de motos:\n")
    file.writelines(lista2)

print("Lista 2 escrita con writelines")

print("Imprimir todo el contenido del archivo")

with open("EjemplArchivo.txt", "r") as file:
    print(file.read())

print("Leer dos líneas y posteriormente 4 caracteres")

with open("EjemplArchivo.txt", "r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline(4))

print("Almacenar el contenido en una lista y mostrar el último elemento")
with open("EjemplArchivo.txt", "r") as file:
    lista = file.readlines()
    print(lista[-1])