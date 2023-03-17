"""
E1
Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha.
Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.

Você deverá aplicar as seguintes funções no exercício:

map

filter

sorted

sum

Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):

a lista dos 5 maiores números pares em ordem decrescente;

a soma destes valores.
"""
with open('number.txt') as arquivo:
    number = list(map(int, map(str.strip, arquivo.readlines())))

cinco_pares = sorted(filter(lambda x: x % 2 == 0, number), reverse=True)[:5]

print(cinco_pares)
print(sum(cinco_pares))

"""
E2
Utilizando high order functions, implemente o corpo da função conta_vogais. 
O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.

É obrigatório aplicar as seguintes funções:

len

filter

lambda

Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.
"""
def conta_vogais(texto:str)-> int:
    vogais = len(list(filter(lambda x: x in 'aAeEiIoOuU', texto)))
    return vogais

"""
E3
A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. 
Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 

Abaixo apresentando uma possível entrada para a função.

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. 

Na lista anterior, por exemplo, teríamos como resultado final 200.

Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:

reduce (módulo functools)

map
"""
from functools import reduce

def calcula_saldo(lancamentos) -> float:
    saldo_final = reduce(lambda saldo, lancamento: saldo + lancamento, map(lambda lancamento: lancamento[0] if lancamento[1] == 'C' else - lancamento[0], lancamentos), 0)
    return saldo_final    

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

print(calcula_saldo(lancamentos))

"""
E4
A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. 
Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. 
Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.

Veja o exemplo:

Entrada

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

Aplicar as operações aos pares de operandos

[ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ] 

Obter o maior dos valores

12

Na resolução da atividade você deverá aplicar as seguintes funções:

max
zip
map
"""

def calcular_valor_maximo(operadores, operandos) -> float:
    operandos0, operandos1 = zip(*operandos)    
    valores = list(map(lambda operando0, operador, operando1: eval(str(operando0) + operador + str(operando1)), operandos0, operadores, operandos1))    
    return max(valores)

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

print(calcular_valor_maximo(operadores, operandos))

"""
E5
Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. 
Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. 
É o arquivo estudantes.csv de seu exercício.

Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:

Nome do estudante

Três maiores notas, em ordem decrescente

Média das três maiores notas, com duas casas decimais de precisão

O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:

Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>

Exemplo:

Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67

Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33

Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:

round

map

sorted
"""
with open('estudantes.csv') as arquivo:
    alunos = sorted(list(map(lambda x: sorted(x.strip('\n').split(','), reverse=True), arquivo)))
    notas = list(map(lambda x: x[1:], alunos)) 
    

with open('estudantes.csv') as arquivo:
    l1 = sorted(list(map(lambda i: sorted(i.strip("\n").split(","), reverse=1), arquivo.readlines())))
    for l in l1:
        notas = sorted([int(i) for i in l[1:]], reverse=1)
        media = sum(notas[:3])/3
    print (f"Nome: {l[0]} Notas: {notas[:3]} Média: {round(media, 2)}")