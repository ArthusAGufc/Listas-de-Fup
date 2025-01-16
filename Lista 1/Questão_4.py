import math
B = 7
C =3.5
A = 2
L = False

a = B == A * C and L or True  #VERDADEIRO
b =  B > A or B == A**A #VERDADEIRO
c = L and B / A >= C or not A <= C #FALSO
d = not L or True and math.sqrt(A+B) >= C #FALSO - errei o certo é True
e = L or B**A <= C * 10 + A * B # VERDADEIRO

print(d)