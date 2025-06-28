import pickle

lista = [35,88,3.14,16]

with open("./Archivos/ArchivoSerial.bin", "wb") as binFile:
  pickle.dump(lista, binFile)

print("Archivo binario escrito")

with open("./Archivos/ArchivoSerial.bin", "rb") as binFile:
  lista2 = pickle.load(binFile)
  print(lista2)

print("Archivo binario leído")