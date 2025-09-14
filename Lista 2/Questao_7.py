"""Faça um programa que receba um caractere e informe se é uma vogal ou não."""

vogais = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

vogal_teste = input("Digite a vogal: ")

if vogal_teste in vogais:
    print("É vogal")
else: 
    print("Não é vogal")