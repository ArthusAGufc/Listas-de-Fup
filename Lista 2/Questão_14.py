""" Faça um programa que receba o código do produto comprado e a quantidade comprada do
 produto. Calcule e mostre o preço unitário do produto comprado, segundo a Tabela I; o preço total
 da nota; o valor do desconto, seguindo a Tabela II e aplicado sobre o preço total da nota; e o preço
 final da nota depois do desconto.
"""

codigo_produto = int(input("Digite o codigo do produto: "))
qtd_produto = int(input("Digite a quantidade do produto: "))

if 1 <= codigo_produto <= 10:
    preco = 10.0
elif 11 <= codigo_produto <= 20:
    preco = 15.0
elif 21 <= codigo_produto <= 30:
    preco = 20.0
elif 31 <= codigo_produto <= 40:
    preco = 40.0

preco_total = preco * qtd_produto

if preco_total <= 250.0:
    desconto = 0.05
    valor = "5%"
elif 250.0 < preco_total <= 500.0:
    desconto = 0.1
    valor = "10%"
elif preco_total > 500.0:
    desconto = 0.15
    valor = "15%"

print(f"Preco Unitario: {preco}\nQtd de produto: {qtd_produto}\nPreco Total: {preco_total}\nValor desconto: {valor}\nDesconto Aplicado: {preco_total * desconto}\nPreço Final: {preco_total - (preco_total * desconto)}\n")