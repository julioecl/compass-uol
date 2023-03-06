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
palavras_originais = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for palavra in palavras_originais:
    if palavra[::-1] == palavra:
        print(f'A palavra: {palavra} é um palíndromo')
    else:
        print(f'A palavra: {palavra} não é um palíndromo')
    
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

arq = open("arquivo_texto.txt")
print(arq.read(),end="")

"""
Exercícios Parte 2 - 12
Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

Dica: leia a documentação do pacote json
"""
import json

arq = open('person.json')
read_file = arq.read()
arq.close()

person = json.loads(read_file)
print(person)
"""
Exercícios Parte 2 - 13
Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.

Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def function(n):
    return n**2   

def my_map(list, f):
    list_2 = []
    for num in list:
        list_2.append(f(num))
    print(list_2)

my_map(lista, function)
    
"""
Exercícios Parte 2 - 14
Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.

Teste sua função com os seguintes parâmetros:

(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
Para organizar o seu código e torná-lo mais legível para a correção, é necessário que você utilize a declaração 'def func()' para definir sua função
"""
def func(*args, **kwargs):
    for arg in args:
        print(arg)
    dict_values = kwargs.values()
    for kwarg in dict_values:
        print(kwarg)

func(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

"""
Exercícios Parte 2 - 15
Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
liga(): muda o estado da lâmpada para ligada
desliga(): muda o estado da lâmpada para desligada
esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
Para testar sua classe:
Ligue a Lampada
Imprima: A lâmpada está ligada? True
Desligue a Lampada
Imprima: A lâmpada ainda está ligada? False
"""
class Lampada:
    def __init__(self, ligada):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada
    
    def desliga(self):
        if self.ligada:
            self.ligada = False
        
    def liga(self):
        if self.ligada == False:
            self.ligada = True
"""
Exercícios Parte 2 - 16
Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.

A string deve ter valor  "1,3,4,6,10,76"
"""
string = "1,3,4,6,10,76"
string_list = string.split(',')
soma = 0
for num in string_list:
    soma = soma + int(num)
print(soma)


"""
Exercícios Parte 2 - 17
Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

sub_lists_len = len(lista)//3
first_list_end = sub_lists_len
second_list_end = first_list_end + sub_lists_len
third_list_end = second_list_end + second_list_end

print(lista[0:first_list_end], lista[first_list_end:second_list_end], lista[second_list_end:third_list_end])
"""
Exercícios Parte 2 - 18
Dado o dicionário a seguir:
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.
"""
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
speed_value = []
for i in speed:
    speed_value.append(speed[i])
speed_set = set(speed_value)

print(list(speed_set))

"""
Exercícios Parte 2 - 19
Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:

Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!

    import random 
    # amostra aleatoriamente 50 números do intervalo 0...500
    random_list = random.sample(range(500),50)

Use as variáveis abaixo para representar cada operação matemática
"""
import random

random_list = random.sample(range(500), 50)
lista_ordenada = sorted(random_list)
meio_da_lista = len(lista_ordenada)//2
mediana = (lista_ordenada[meio_da_lista] + lista_ordenada[meio_da_lista-1]) / 2
media = sum(random_list)/50
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')

"""
Exercícios Parte 2 - 20
Imprima a lista abaixo de trás para frente.

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""
a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
reversed_a = a[::-1]
print(reversed_a)