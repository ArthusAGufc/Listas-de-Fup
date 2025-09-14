""" Dados três valores A, B e C, verificar se eles podem ser valores dos lados de um triângulo e, se
 forem, verificar se é um triângulo escaleno, equilátero ou isósceles. Dicas:
 • O lado de um triângulo não pode ser maior ou igual do que a soma dos outros dois.
 • Um triângulo equilátero possui os três lados iguais.
 • Um triângulo isósceles possui dois lados iguais.
 • Um triângulo escaleno possui os três lados diferentes."""

valor_A = float(input("Digite valor A: "))
valor_B = float(input("Digite valor B: "))
valor_C = float(input("Digite valor C: "))

if (valor_A < valor_B + valor_C) and (valor_B < valor_A + valor_C) and (valor_C < valor_A + valor_B):
    if valor_A == valor_B == valor_C:
        print("equilátero")
    elif (valor_A == valor_B) or (valor_A == valor_C) or (valor_B == valor_C):
        print("isósceles")
    else:
        print("escaleno")
else: 
    print("Lado maior que soma dos outros")