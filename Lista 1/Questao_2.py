"""
 Calcule o resultado das expressões, sabendo que A = 5, B = 10, C = – 8 e D = 1.5.
 a) 2 * A % 3 – C
 b) math.sqrt( – 2 * C) / 4
 c) ((20 / 3) / 3) + 8**2 / 2
 d) 5 * 3 + 15 % 5 + 8 – 1 * 20 / 15
 e) math.sqrt( A**(A / B) ) + C * D
 f) 5**2 – math.sqrt(125) * 0 / 540 – 10 / 2
"""
import math

# Variaveis globais
A = 5 
B = 10
C = -8 
D = 1.5

item_a = 2 * A % 3 - C
item_b = math.sqrt(-2 * C)/4
item_c = ((20/3)/3) + 8**2 / 2
item_d = 5 * 3 + 15 % 5 + 8 - 1 * 20 / 15
item_e = math.sqrt( A**(A / B) ) + C * D
item_f = 5**2 - math.sqrt(125) * 0 / 540 - 10 / 2

print("ITEM A:", item_a)
print("ITEM B:", item_b)
print("ITEM C:", item_c)
print("ITEM D:", item_d)
print("ITEM E:", item_e)
print("ITEM F:", item_f)