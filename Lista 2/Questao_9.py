"""Escreva um programa que receba três números e escreva eles em ordem crescente."""

numero_1 = int(input("Digite Primeiro numero: "))
numero_2 = int(input("Digite Segundo numero:  "))
numero_3 = int(input("Digite Terceiro numero: "))

if numero_1 > numero_2  and numero_1 > numero_3:
    if numero_2 > numero_3:
        print(f"{numero_3} {numero_2} {numero_1}")
    else:
        print(f"{numero_2} {numero_3} {numero_1}")
elif numero_2 > numero_1  and numero_2 > numero_3:
    if numero_1 > numero_3:
        print(f"{numero_3} {numero_1} {numero_2}")
    else:
        print(f"{numero_1} {numero_3} {numero_2}")
else:
    if numero_1 > numero_2:
        print(f"{numero_2} {numero_1} {numero_3}")
    else:
        print(f"{numero_1} {numero_2} {numero_3}")