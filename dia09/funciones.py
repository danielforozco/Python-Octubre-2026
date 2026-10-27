"""
1 - Crea una función que dibuje un cuadro con con la altura y anchura indicada.
2 - Crea una función que dibuje un rectángulo con la altura y anchura indicada.
3 - Crea una función que dibuje un cuadro hueco con con la altura y anchura indicada.
4 - Crea una función que dibuje un rectángulo hueco con la altura y anchura indicada.
5 - Dibuja un triangulo con la altura y anchura indicada.
"""

import os

os.system("cls")

def cuadrado(num):
    for i in range(num):
        print("* " * num)

def rectangulo(altura, anchura):
    for i in range(altura):
        print("* " * anchura)

def cuadrado_hueco(num):
    for i in range(num):
        if i == 0 or i == num - 1:
            print("* " * num)
        else:
            print("* " + "  " * (num - 2) + "*")

def rectangulo_hueco(altura, anchura):
    for i in range(altura):
        if i == 0 or i == altura - 1:
            print("* " * anchura)
        else:
            print("* " + "  " * (anchura - 2) + "*")

def triangulo_altura_anchura(altura, anchura):
    for i in range(altura):
        espacios = " " * (altura - i - 1)
        asteriscos = "* " * (i + 1)
        print(espacios + asteriscos)

cuadrado(5)
print()
rectangulo(3, 7)
print()
cuadrado_hueco(5)
print()
rectangulo_hueco(3, 7)
print()
triangulo_altura_anchura(5, 7)
