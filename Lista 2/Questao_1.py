"""Faça um programa que receba dois números e diga o maior deles. Caso sejam iguais, o programa
 deve ser capaz de informar isto."""

numero_1 = float(input("Digite primeiro numero: "))
numero_2 = float(input("Digite segundo numero: "))

if numero_1 > numero_2:
    print(f"{numero_1} e maior que {numero_2}")
elif numero_1 < numero_2:
    print(f"{numero_2} e maior que {numero_1}")
else:
    print(f"{numero_1} e igual a {numero_2}")