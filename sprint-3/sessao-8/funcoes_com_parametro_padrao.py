"""
Funções com parâmetro padrão - (default parameters)

Parâmetro(s) padrão(s) deve(m) estar sempre por último na declaração de função.

Por que usar?

Permite uma flexibilidade maior nas funções.
Evita erro com parâmetros incorretos.
Permite trabalhar com exemplos mais legíveis de código.

Escopo
 - Variáveis globais: Fora do escopo da função
    obs: se puder evitar, melhor.
 - Variáveis locais: Somente dentro do escopo que se encontra.
    obs: para chamar uma variável global, informar global antes do nome

    total = 0

    def incrementa():
        global total
        total = total + 1
        return total

    print(incrementa())


"""
def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(5)) # Como potencia tem o valor padrão 2, caso não for informado, ele será 2.
print(exponencial(2, 3)) # Caso seja passado o argumento, ele recebe esse valor.

def mostra_infomacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você fosse instrutor!'
    return f'Olá {nome}'

print(mostra_infomacao()) # Assume os parâmetros padrões
print(mostra_infomacao(instrutor=True)) # Assume o parâmetro padrão para nome e True para instrutor.
print(mostra_infomacao('Ozzy')) # Caso tiver 2 parâmetros na função e passar somente 1 argumento, esse passará para o primeiro.

# Usando função como parâmetro

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

print(mat(2, 3)) # Por padrão, chama a função soma
print(mat(2, 2, subtracao)) # Informando um argumento para o parâmetro padrão, então assume outra função e não mais soma.

# Funções dentro de funções

def fora():
    contador = 0
    def dentro():
        nonlocal contador # Nem local, nem global, referente a função anterior
        contador = contador + 1
        return contador
    return dentro()

print(fora())