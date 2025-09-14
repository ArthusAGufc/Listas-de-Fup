""") Escreva um programa que receba do usuário as coordenadas (x,y) de três pontos A, B e C e faça
 o que se pede:
 • Verifique se os pontos A e B podem formar um retângulo como mostrado na figura abaixo,
 ou seja, o ponto A ser um canto inferior esquerdo e B um canto superior direito de um
 retângulo. O programa deve informar se isto é possível.
 • Caso o retângulo seja possível, informe se o ponto C é interno ao retângulo ou não."""

cooordenada_x_A = float(input("Coordenada x A: "))
cooordenada_y_A = float(input("Coordenada y A: "))

cooordenada_x_B = float(input("Coordenada x B: "))
cooordenada_y_B = float(input("Coordenada y B: "))

cooordenada_x_C = float(input("Coordenada x C: "))
cooordenada_y_C = float(input("Coordenada x C: "))

if (cooordenada_x_A == cooordenada_y_B) or (cooordenada_y_A == cooordenada_x_B):
    print("NAO FORMA RETANGULO")
else:
    if (cooordenada_x_C > cooordenada_x_A) and (cooordenada_y_C > cooordenada_y_A):
        if (cooordenada_x_C < cooordenada_x_B) and (cooordenada_y_C < cooordenada_y_B):
            print("DENTRO")
    else: 
        print("FORA")
