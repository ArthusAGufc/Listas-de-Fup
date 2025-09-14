"""Escreva um programa que leia os coeficientes a, b e c de uma equação do segundo grau
 ax2+bx+c e faça as seguintes verificações:
 • se o coeficiente a for igual a zero, imprima a mensagem “Não é equação do segundo grau”
 • se Δ<0, não existe raiz real, então imprima a mensagem “Não existe raiz real.”
 • se Δ=0, existe uma raiz real, então imprima a mensagem “Raiz única.” e o valor dessa
 raiz.
 • se Δ>0, existe duas raízes reais, então imprima a mensagem “Duas raízes.” e os valores
 dessas raízes.
 Lembrando que Δ=b2−4ac e as raízes da equação são dadas por: x=−b±√
 Δ
 2a """

import math 
coeficiente_a = float(input("Coeficiente A: "))
coeficiente_b = float(input("Coeficiente B: "))
coeficiente_c = float(input("Coeficiente C: "))

delta = (coeficiente_b ** 2) - 4 * coeficiente_a * coeficiente_c

if coeficiente_a == 0:
    print("Não é equação do segundo grau")
elif delta < 0:
    print("Não existe raiz real")
elif delta == 0:
    raiz_1 = -coeficiente_b + math.sqrt(delta) * (2 * coeficiente_a)
    print("Raiz única", raiz_1)
else:
    raiz_1 = -coeficiente_b + math.sqrt(delta) * (2 * coeficiente_a)
    raiz_2 = -coeficiente_b - math.sqrt(delta) * (2 * coeficiente_a)
    print("Duas raízes", raiz_1, raiz_2)






