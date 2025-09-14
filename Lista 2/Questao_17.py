"""Escreva um programa que leia as coordenadas (x,y) de um ponto e informe a qual quadrante ele
 pertence segundo a figura abaixo."""

cooordenada_x = float(input("Coordenada x: "))
cooordenada_y = float(input("Coordenada y: "))

if cooordenada_x == 0 and cooordenada_y == 0:
    print(f"({cooordenada_x},{cooordenada_y}) origem do plano")
elif cooordenada_x > 0 and cooordenada_y > 0:
    print(f"({cooordenada_x},{cooordenada_y}) 1 QUADRANTE")
elif cooordenada_x < 0 and cooordenada_y > 0:
    print(f"({cooordenada_x},{cooordenada_y}) 2 QUADRANTE")
elif cooordenada_x < 0 and cooordenada_y < 0:
    print(f"({cooordenada_x},{cooordenada_y}) 3 QUADRANTE")    
else:
    print(f"({cooordenada_x},{cooordenada_y}) 4 QUADRANTE")   