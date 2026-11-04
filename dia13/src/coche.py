from vehiculo import vehiculo

class Coche(vehiculo):
    def __init__(self, marca, modelo, precio_dia, motor, num_puertas):
        super().__init__(marca, modelo, precio_dia, motor)
        self.num_puertas = num_puertas

    def calcular_alquiler(self, dias):
        total_recargo = 0
        if