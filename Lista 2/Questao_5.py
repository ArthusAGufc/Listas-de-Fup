"""Crie uma versão do programa da questão 4 de forma que informe se o aluno está aprovado
 (média maior ou igual a 7), reprovado (média menor do que 4) ou em recuperação (média maior ou
 igual a 4 e menor do que 7)."""

nota_1 = float(input("Digite Primeira Nota: "))
nota_2 = float(input("Digite Segunda Nota:  "))
nota_3 = float(input("Digite Terceira Nota: "))

if (0.0 <= nota_1 <= 10.0) and (0.0 <= nota_2 <= 10.0) and (0.0 <= nota_3 <= 10.0):
    media = (nota_1 + nota_2 + nota_3) / 3
    if media >= 7.0:
        print(f"APROVADO - Media final: {media:.2f}")
    elif 4.0 <= media < 7.0:
        print("RECUPERAÇÃO")
    else:
        print("REPROVADO")
else:
    print("Digite valores entre 0 e 10")