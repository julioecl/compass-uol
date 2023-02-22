"""
Exercícios Parte 1 - 1 
Escreva um código Python que lê do teclado o nome e a idade de um usuário e que imprima apenas o ano em que ele completará 100 anos.

Dica: você pode ler strings digitadas no teclado utilizando a função builtin input('mensagem'). Lembre-se de converter números para seu respectivo tipo (int ou float) antes fazer operações aritméticas.
"""
import datetime

name = input('Digite seu nome: ')
age = int(input('Digite sua idade: '))

def hundred_years(age):
    today = datetime.date.today()
    year = today.year
    return year + (100 - age)    

print(hundred_years(age))

"""
Exercícios Parte 1 - 2
Escreva um código Python que verifique se três números digitados pelo usuário são pares ou ímpares. Para cada número, imprima o Par: ou Ímpar: e o número correspondente.

Exemplo de formato de saída:

Par: 2

Ímpar: 3
"""
lista = []
num1 = int(input('Digite um número: '))
lista.append(num1)
num2 = int(input('Digite um número: '))
lista.append(num2)
num3 = int(input('Digite um número: '))
lista.append(num3)

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        print('Par:', lista[i])
    else:
        print('Ímpar:', lista[i])
"""
Exercícios Parte 1 - 3
Escreva um código Python que imprime os números pares de 0 até 20 (incluso).

Dica: Utilize a função range().
"""
for n in range(21):
    if n % 2 == 0:
        print(n)

"""
Exercícios Parte 1 - 4
Escreva um código Python que imprime todos os números primos de 1 até 100. Abaixo uma imagem de exemplo dos números primos entre 1 e 1000.
Obs: Utilize a função range().
"""    
for n in range(1,101):
    if n != 1:
        if n == 2 or n == 3 or n == 5 or n == 7:
            print(n)
        elif n % 2 != 0:
            if n % 3 != 0:
                if n % 5 != 0:
                    if n % 7 != 0:
                        print(n)
"""
Exercícios Parte 1
Escreva um código Python que tem 3 variáveis dia (22), mês(10) e ano(2022) e imprime a data completa no formato a seguir:

Exemplo: 22/10/2022

Importante: É necessário formatar as variáveis como strings antes de concatená-las e imprimi-las na tela.
"""
day = str(22)
month = str(10)
year = str(2022)

print(day + '/' + month + '/' + year)