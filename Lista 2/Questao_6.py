"""Uma universidade avalia seus cursos através de diversos fatores e atribui uma nota de 0 a 10 ao
 final da avaliação. Para fins de divulgação, os cursos são classificados segundo uma classificação
 descrita na tabela abaixo:

Escreva um programa que converta a nota de um curso em seu conceito."""

nota_geral = float(input("Digite a Nota Geral: "))

if 0.0 <= nota_geral <= 10.0:
    if 8.0 <= nota_geral <= 10.0:
        print(f"NOTA GERAL A: {nota_geral:.2f}")
    elif 7.0 <= nota_geral < 8.0:
        print(f"NOTA GERAL B: {nota_geral:.2f}")
    elif 6.0 <= nota_geral < 7.0:
        print(f"NOTA GERAL C: {nota_geral:.2f}")
    elif 5.0 <= nota_geral < 6.0:
        print(f"NOTA GERAL D: {nota_geral:.2f}")
    else:
        print(f"NOTA GERAL E: {nota_geral:.2f}")
else:
    print("Digite valores entre 0 e 10")

