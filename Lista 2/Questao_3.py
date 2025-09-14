"""Faça um programa que receba dois números inteiros A e B e informe que A é múltiplo de B ou
 não."""

numero_inteiro_1 = int(input("Digite o primeiro numero inteiro: "))
numero_inteiro_2 = int(input("Digite o segundo numero inteiro: "))


resto = numero_inteiro_1 % numero_inteiro_2
if resto == 0:
    print(f"{numero_inteiro_1} e multiplo de {numero_inteiro_2}")
else:
    print(f"{numero_inteiro_1} nao e multiplo de {numero_inteiro_2}")