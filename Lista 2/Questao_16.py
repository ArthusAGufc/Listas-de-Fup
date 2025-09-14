"""Faça um programa que receba o valor do salário-base e o  número de dependentes de um
 determinado funcionário e calcule e mostre o salário a receber do funcionário de acordo com as
 regras a seguir:
 • Para cada dependente, acrescentar R$120,00.
 • O salário bruto é igual ao salário-base mais o valor dos dependentes.
 • Calcular o valor do imposto de renda retido na fonte (IRRF) de acordo com a tabela:
 IRRF Salário Bruto
 Isento Inferior a R$1000,00
 10% De R$1000,00 até R$ 2500,00
 20% Superior a R$2500,00
 • O salário líquido é igual ao salário bruto menos o IRRF.
 • A gratificação é de acordo com a tabela a seguir:
 Salário Líquido
 Gratificação
 Até R$1750,00
 R$ 500,00
 Superior a R$1750,00 R$ 250,00
 • O salário a receber do funcionário é igual ao salário líquido mais a gratificação.
"""

salario_base = float(input("Salário-base: "))
num_depedentes = int(input("Número de dependentes: "))

extra_depedentes = 120.0 * num_depedentes
salario_bruto = salario_base + extra_depedentes

if salario_bruto < 1000.0:
    salario__liguido = salario_bruto - 0
elif 1000.0 <= salario_bruto <= 2500.0:
    salario__liguido = salario_bruto - (salario_bruto * (10/100))
elif salario_bruto > 2500.0:
    salario__liguido = salario_bruto - (salario_bruto * (20/100))

if salario__liguido <= 1750:
    salario_final = salario__liguido + 500.0
else:
    salario_final = salario__liguido + 250.0

print(f"Salario Final: {salario_final}")
