"""Muitos bancos possuem o serviço do crédito rotativo do cartão de crédito. Ele é um serviço que
 pode ser acionado pela pessoa que não pode pagar o valor total da fatura no vencimento, mas não
 quer ficar inadiplente. Para usar o crédito rotativo, o consumidor paga qualquer valor entre o
 mínimo e o total da fatura. O restante é lançado no mês seguinte, com juros. Muitos bancos cobram
 o valor de 3,3% de juros neste serviço. Escreva um programa que leia o valor usado por um cliente
 no mês de Março, o valor que ele pagou dessa fatura, o valor usado por este cliente no mês de Abril
 e retorne o valor da fatura do mês de Abril.
 Ex:
 Valor usado no mês de Março: 200
 Valor pago no mês de Março: 20
 Valor usado no mês de Abril: 150
 Fatura do mês de Abril: 150 + 180 + 180*(3,3%) = 335,94"""

valor_usado_marco = float(input("Valor usado no mês de Março: "))
valor_pago_marco = float(input("Valor pago no mês de Março: "))
valor_usado_abril = float(input("Valor usado no mês de Abril: "))

acumulacao_fatura = valor_usado_marco - valor_pago_marco
fatura_abril = valor_usado_abril + acumulacao_fatura + (acumulacao_fatura * (3.3 / 100))

print("Fatura do mês de Abril:", fatura_abril)