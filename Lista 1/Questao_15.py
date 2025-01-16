"""Escreva um programa que leia as coordenadas de dois pontos e retorne a distância entre eles."""

import math
coordenada_ponto1_x = int(input("Coordenada ponto 1(A) - x: "))
coordenada_ponto1_y = int(input("Coordenada ponto 1(A) - y: "))

coordenada_ponto2_x = int(input("Coordenada ponto 2(B) - x: "))
coordenada_ponto2_y = int(input("Coordenada ponto 2(B) - y: "))

distancia_entre_pontos = math.sqrt(math.pow((coordenada_ponto1_x - coordenada_ponto2_x), 2) + math.pow((coordenada_ponto1_y - coordenada_ponto2_y), 2))

print("Distancia entre A e B: ", distancia_entre_pontos)