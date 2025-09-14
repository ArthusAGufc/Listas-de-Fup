"""Muitos supermercados vendem o mesmo produto com tamanhos e preços diferentes. Por
 exemplo: Leite Ninho de 200g a R$5,00 e Leite Ninho de 1Kg a R$23,00. No caso deste exemplo, é
 mais vantajoso proporcionalmente para o cliente comprar o Leite Ninho de 1Kg. Escreva um
 programa que leia as gramas e preços de um determinado produto e retorne indicando a versão
 proporcionalmente mais barata ao cliente.
 Ex:
 produto: Leite Ninho
 massa da versao 1: 200
 preco da versao 1: 5
 massa da versao 2: 1000
 preco da versao 2: 23
 Resultado: Leite Ninho de 1000g por R$23.00 eh mais vantajoso."""

produto = input("Digite nome do produto: ")
massa_versao1 = float(input("Massa versão 1: "))
preco_versao1 = float(input("Preço versão 1: "))
massa_versao2 = float(input("Massa versão 2: "))
preco_versao2 = float(input("Preço versão 2: "))

relacao_versao1 = massa_versao1 / preco_versao1
relacao_versao2 = massa_versao2 / preco_versao2

if relacao_versao1 > relacao_versao2:
    print(f"{produto} de {massa_versao1} por {preco_versao1} é mais vantajoso")
elif relacao_versao1 < relacao_versao2:
    print(f"{produto} de {massa_versao2} por {preco_versao2} é mais vantajoso")
else:
    print(f"ambos servem")