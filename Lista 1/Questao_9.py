"""Escreva um programa que leia os coeficientes A, B e C de uma equação Ax2+Bx+C=0 e calcule
 o valor do discriminante delta e as raízes da equação."""

import math 
coeficiente_a = float(input("Coeficiente A: "))
coeficiente_b = float(input("Coeficiente B: "))
coeficiente_c = float(input("Coeficiente C: "))

delta = (coeficiente_b ** 2) - (4 * coeficiente_a * coeficiente_c)

if delta < 0:
    print("Nao possui raizes reais")
else:
    raiz_1 = ((-1 * coeficiente_b) + math.sqrt(delta)) / 2 * coeficiente_a
    raiz_2 = ((-1 * coeficiente_b) - math.sqrt(delta)) / 2 * coeficiente_a
    print(f"Delta: {delta}, Raiz 1: {raiz_1}, Raiz 2: {raiz_2}")