class Vehiculo:
    def __init__(self, marca, modelo, precio_dia, motor):
        self.marca = marca
        self.modelo = modelo
        self.precio_dia = precio_dia
        self.motor = motor

    def calcular_alquiler(self, dias):
        return self.precio_dia * dias

    def __str__(self):
        return f"Vehiculo: {self.marca} {self.modelo}, {self.motor}"