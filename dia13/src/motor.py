class Motor:
    def __init__(self, tipo_combustible, potencia_hp):
        self.tipo_combustible = tipo_combustible
        self.potencia_hp = potencia_hp

    def __str__(self):
        return f"Motor: {self.tipo_combustible}, {self.potencia_hp} HP"