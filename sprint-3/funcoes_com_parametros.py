"""
Funções com parametro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

fluxo: entrada -> processamento -> saída

Em caso de mais parâmetros, a mesma ordem ao declarar e ao invocar a função é seguida.

Na função chamamos de parâmetros: "n" e "e" 

def expoenciacao(n, e):
    return n**e

Na chamada da função, são argumentos: 5 e 3 são argumentos

print(expoenciacao(5,3))

Argumentos nomeado (keyword arguments)

Se utilizar argumentos nomeados, não há importância em qual ordem eles são informados:

print(expoenciacao(e=10,n=7))

numero = 7
expoente = 5
print(expoenciacao(n=numero,e=expoente))

"""

def expoenciacao(n, e):
    return n**e

numero = 7
expoente = 5

print(expoenciacao(numero, expoente))
print(expoenciacao(n=numero,e=expoente))
print(expoenciacao(e=10,n=7))