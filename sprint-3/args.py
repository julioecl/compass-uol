"""
Entendendo o *args

Por convenção, foi adotado o nome *args.

O parâmetro *args utilizado em uma função coloca os valores extras informados como entrada em uma tupla.
Ou seja, tulas são imutáveis.

*args como parâmetro quer dizer que não é especificado quantos argumentos precisa informar para chamar a função, pode ser 0 ou até mil.
"""

def soma_todos_valores(*args):
    return sum(args)

print(soma_todos_valores())
print(soma_todos_valores(1, 2, 3, 5))

# Por padrão, caso informe uma lista como arg, o python considera que toda a lista é um elemento e não cada elemento dentro da lista é um elemento
# Para fazer que seja considerado o valor individual, informamos a lista com um *.
# Esse comando desempacota a lista em valores individuais.

numeros = [1, 2, 3, 4, 5, 6]

def soma_todos_valores(*args):
    return sum(args)

print(soma_todos_valores(*numeros))

