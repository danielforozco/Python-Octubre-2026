from scr.coche import Coche
from scr.motocicleta import Motocicleta

def generar_resumen_alquiler(vehiculo, dias):
    total_alquiler = vehiculo.calcular_alquiler(dias)
    return f"Resumen del alquiler:\nVehículo: {vehiculo.marca} {vehiculo.modelo}\nDías: {dias}\nTotal a pagar: ${total_alquiler:.2f}"

motor_motoci