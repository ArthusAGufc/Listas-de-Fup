""" Escreva um programa que leia a altura e o raio da base de um cilindro circular reto e escreva as
 seguintes informações: área lateral, área da base e volume.
 Comprimentodacircunferência = 2π × raio
 Áreadacircunferência = π × raio2
 Volumedocilindro = Áreadabase × Altura"""

Pi = 3.14
altura_cilindro = float(input("Altura cilindro: "))
raio_cilindro = float(input("Raio da base cilindro: "))

comprimento_circuferencia = 2 * Pi * raio_cilindro
area_da_circuferencia = Pi * (raio_cilindro ** 2)
volume_cilindro = area_da_circuferencia * altura_cilindro

print("Comprimento da circunferência: ",comprimento_circuferencia)

print("Área da circunferência: ", area_da_circuferencia)
print("Volume do cilindro: ", volume_cilindro)
