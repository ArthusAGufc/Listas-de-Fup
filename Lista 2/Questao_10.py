""" Escreva um programa tenha o seguinte menu de opções:
 1. soma
 2. subtração
 3. multiplicação
 4. divisão
 O usuário deve ser capaz de escolher uma dessas opções digitando o número correspondente e
 depois inserir os valores a serem usados na operação desejada. Depois o programa escreve a
 resposta.
"""
valor_1 = float(input("Digite valor 1: "))
valor_2 = float(input("Digite valor 2: "))
escolha = int(input(("1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão ")))

if escolha == 1:
    soma = valor_1 + valor_2
    print(soma)
elif escolha == 2:
    subtracao = valor_1 - valor_2
    print(subtracao)
elif escolha == 3:
    multiplicacao = valor_1 * valor_2
    print(multiplicacao)
elif escolha == 4:
    divisao = valor_1 / valor_2
    print(escolha)
else:
    print("Escolha invalida")



