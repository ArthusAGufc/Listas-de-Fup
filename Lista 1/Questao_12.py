"""Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula da conversão é
 R=G⋅(π /180) , sendo G o ângulo em graus e R em radianos. (Obs: defina uma constante para o
 valor de π )."""

CONST_PI = 3.14
angulo_graus = float(input("Ângulo em graus: "))

conversao_GrausRad = angulo_graus * (CONST_PI / 180)

print(f"Hipotenusa: {conversao_GrausRad}")