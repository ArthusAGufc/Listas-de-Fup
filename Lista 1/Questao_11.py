""" Escreva um programa que leia os dois catetos de um triângulo retângulo e retorne o valor da
 hipotenusa."""

cateto_a = float(input("Cateto A: "))
cateto_b = float(input("Cateto B: "))

hipotenusa = (cateto_a ** 2) + (cateto_b ** 2)

print(f"Hipotenusa: {hipotenusa}")