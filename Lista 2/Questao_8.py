"""Faça um programa que receba três números inteiros e retorne o maior número dentre os três."""

numero_1 = int(input("Digite Primeiro numero: "))
numero_2 = int(input("Digite Segundo numero:  "))
numero_3 = int(input("Digite Terceiro numero: "))

if numero_3 < numero_1 > numero_2:
    print(f"{numero_1} é maior que {numero_2} e {numero_3}")
elif numero_3 < numero_2 > numero_1:
    print(f"{numero_2} é maior que {numero_1} e {numero_3}")
else:
    print(f"{numero_3} é maior que {numero_1} e {numero_2}")
