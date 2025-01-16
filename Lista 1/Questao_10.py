"""Escreva um programa que leia os coeficientes A, B, e C e um valor x e retorne o resultado de
 sua aplicação na função f (x)=Ax2+Bx+C ."""

import math 
coeficiente_a = float(input("Coeficiente A: "))
coeficiente_b = float(input("Coeficiente B: "))
coeficiente_c = float(input("Coeficiente C: "))
valor_x = float(input("Valor de x: "))

equacao = (coeficiente_a * (valor_x ** 2)) + (coeficiente_b * valor_x) + coeficiente_c

print(f"Equação: {equacao}")