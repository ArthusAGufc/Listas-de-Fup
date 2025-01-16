"""Escreva um programa que leia as coordenadas (x,y) de um ponto e retorne a sua distância até a
 origem do sistema de coordenadas.
"""
import math
coordenada_x = int(input("Coordenada x: "))
coordenada_y = int(input("Coordenada y: "))

distancia_pra_origem = math.sqrt((coordenada_x ** 2) + (coordenada_y ** 2))

print("Distancia para a origem: ", distancia_pra_origem)