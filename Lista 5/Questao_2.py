"""Escreva uma função palindromo(s) que retorna verdadeiro ou falso, caso a string entrada seja
 um palíndromo. (Palíndromos são palavras ou frases que são iguais tanto da esquerda pra direita
 como da direita pra esquerda).
 Ex:
 palindromo("bemtevi") →  False
 palindromo("arara") → True """



def palindromo(string):
    tam = len(string)

    for i in string(-1):
        print(i)
    
palindromo('yvens')