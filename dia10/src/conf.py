from src.cacl import sum, subtract, multiply, divide, table_multiplication

def config():
    data = [
        {"text": "Sumar", "function": sum, "values": 2},
        {"text": "Restar", "function": subtract, "values": 2},
        {"text": "Multiplicar", "function": multiply, "values": 2},
        {"text": "Dividir", "function": divide, "values": 2},
        {"text": "Tabla de multiplicar", "function": table_multiplication, "values": 1},
    ]

    return list(map(lambda x: {**x[1], "order": x[0] + 1}, enumerate(data)))