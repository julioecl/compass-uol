"""
Exercícios Parte 2 - 6
Dada duas listas como as no exemplo abaixo:



a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


Escreva um programa que retorne o que ambas as listas têm em comum (sem repetições). O seu programa deve funcionar para listas de qualquer tamanho.
"""
a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

intersection = set(a).intersection(set(b))
print(list(intersection))

"""
Exercícios Parte 2 - 7
Dada a seguinte lista:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Faça um programa que gere uma nova lista contendo apenas números ímpares.
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
impares = []

for i in range(len(a)):
    if a[i] % 2 != 0:
        impares.append(a[i])

print(impares)

"""
Exercícios Parte 2 - 8
Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.
Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.
É necessário que você imprima no console exatamente assim:
A palavra: maça não é um palíndromo
 
A palavra: arara é um palíndromo
 
A palavra: audio não é um palíndromo
 
A palavra: radio não é um palíndromo
 
A palavra: radar é um palíndromo
 
A palavra: moto não é um palíndromo
"""


"""
Exercícios Parte 2 - 9
Dada as listas a seguir:

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".

Exemplo:

0 - João Soares está com 19 anos
Você deve Utilizar a função enumerate().

"""
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, primeiroNome in enumerate(primeirosNomes):
    print(i, '-', primeiroNome, sobreNomes[i], 'está com', idades[i], 'anos')

"""
Exercícios Parte 2 - 10
Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.

['abc', 'abc', 'abc', '123', 'abc', '123', '123']
"""

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

lista2 = set(lista)

print(list(lista2))

"""
Exercícios Parte 2 - 11
Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

Dica: leia a documentação da função open(...)
"""

"""
Exercícios Parte 2 - 12
Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

Dica: leia a documentação do pacote json
"""


"""
Exercícios Parte 2 - 13
Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.



Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.
"""