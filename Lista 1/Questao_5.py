"""Crie um programa que permita fazer a conversão cambial entre Dólares e Reais. Considere como
 taxa de câmbio US$ 1,00 = R$ 3,92. Leia um valor em Dólares pelo teclado e mostre o
 correspondente em Reais."""

valor_dolar = float(input(("Digite valor em Dollar US$: ")))
valor_reais = valor_dolar * 3.92
print(f"US$ {valor_dolar} equivale a R$ {valor_reais}")