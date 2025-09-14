"""Faça um programa que receba um número inteiro e imprima se o número é par ou ímpar."""

numero_inteiro = int(input("Digite o umero inteiro para saber sua paridade: "))

resto_divisao = numero_inteiro % 2

if resto_divisao == 0:
    print(f"{numero_inteiro} é par")
else: 
    print(f"{numero_inteiro} é impar")   