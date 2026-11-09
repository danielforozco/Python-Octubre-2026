def sum(a, b):
    print(f"{a} + {b} = {a + b}")

def subtract(a, b):
    print(f"{a} - {b} = {a - b}")

def multiply(a, b):
    print(f"{a} * {b} = {a * b}")

def divide(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    print(f"{a} / {b} = {a / b}")

def table_multiplication(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")