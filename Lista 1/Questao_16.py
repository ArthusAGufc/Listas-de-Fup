""" O imposto brasileiro sobre acessórios de video-games é de 40%. Escreva um programa que leia
 o valor de um acessório e retorne a quantia repassada ao governo por imposto."""

taxa = 40/100
valor_acessorio = float(input("Valor do acessório: "))
valor_do_imposto = valor_acessorio * taxa

print("Valor do acessorio com imposto: ", valor_do_imposto + valor_acessorio)