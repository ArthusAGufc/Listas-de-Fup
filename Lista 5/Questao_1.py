"""Escreva uma função inverte(s) que recebe uma string s e retorna a os caracteres da string de
 trás para frente. Não use a função reverse da linguagem Python. 
 Ex: inverte("Russas") → "sassuR"""

def inverte(string_s):
    mensagem = ""
    for i in range(1, len(string_s)+1):
        mensagem += string_s[-i]
    return mensagem
     
x = inverte("amor de mae")
print(x)