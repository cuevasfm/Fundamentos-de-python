class Automovil:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def avanzar(self):
        print(f"El automovil {self.marca} avanza")

    def retroceder(self):
        print(f"El automovil {self.marca} retrocede y es de color {self.color}")

if __name__ == "__main__":
    auto = Automovil("Toyota", "Rojo")
    auto.avanzar()
    auto.retroceder()

    auto2 = Automovil("Ford", "Azul")
    auto2.retroceder()
