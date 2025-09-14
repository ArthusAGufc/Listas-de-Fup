"""Faça um programa que leia 3 notas, verifique se as notas são válidas (um valor entre 0 e 10) e
 exiba na tela a média dessas notas em duas casas decimais. Se pelo menos uma das notas não for
 válida, a média não é calculada e uma mensagem de erro deve ser exibida."""


nota_1 = float(input("Digite Primeira Nota: "))
nota_2 = float(input("Digite Segunda Nota:  "))
nota_3 = float(input("Digite Terceira Nota: "))

if (0.0 <= nota_1 <= 10.0) and (0.0 <= nota_2 <= 10.0) and (0.0 <= nota_3 <= 10.0):
    media = nota_1 + nota_2 + nota_3 / 3
    print(f"Media final: {media:.2f}")
else:
    print("Digite valores entre 0 e 10")

    
    

