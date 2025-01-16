"""
3) Suponha que o símbolo ÷ divide dois números e retorna o número inteiro resultado da divisão
 sem a parte fracionária e o símbolo  /  divide dois números e retorna um valor real com a resposta
 exata. Ambos os operadores  possuem a mesma precedência. Sabendo que os valores das variáveis
 são X = – 1, Y = 3 e Z = 7, calcule os resultados das seguintes atribuições.
 a) Y←Y+1
 b) Y ←Y+3
 c) Media←(X+Y+Z)/3
 d) Media←X+Y+Z/3
 e) K←Z÷Y/3
 f) K←(Z÷Y)/3
 g) K←Z÷(Y/3)
"""

X = -1
Y = 3
Z = 7

Y = Y + 1
print("ITEM A:",Y)

Y = Y + 3
print("ITEM B:", Y)

media = (X + Y + Z) / 3
print("ITEM C:", media)

media = X + Y + Z / 3
print("ITEM D:", media)

K = Z // Y / 3
print("ITEM E:", K)

K = (Z // Y) / 3
print("ITEM F:", K)

K = Z // (Y / 3)
print("ITEM G:", K)






