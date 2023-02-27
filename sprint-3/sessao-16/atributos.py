"""
POO - Atributos

Atributos representam as características do objeto.
Pelos atributos conseguimos representar computacionalmente os estados de um objeto.

Atributos de instância:
Atributos de classe:
Atributos Dinâmicos:

Atributos são publicos por convenção, mas podem ser privados. Para isso, antes do atributo,
colocar __ (duplos underscore)
    ex:
    class Lampada:
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    Usando name mangling consegue-se acesso ao atributo privado: _NomeDaClasse__atributoPrivado    
    
"""
## Atributos de instância: São declarados dentro do método construtor.

class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem # atributos de instância
        self.cor = cor
        self.ligada = False

class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao 
        self.valor = valor

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.limite = limite
        self.numero = numero
        self.saldo = saldo

led = Lampada('220v', 'Amarela')

print(led.voltagem)

# Atributos de classe: São declarado diretamente na classe, fora do construtor.
# Geralmente é iniciado com um valor que é compartilhado com todas as instâncias.

class Produto:

    imposto = 1.05 # atributo de classe
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao 
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id # altera o valor do contador (atributo de classe) para o id do produto, para seguir a contagem

p1 = Produto('Ps5', 'Video Game', 5000)
p2 = Produto('Xbox', 'Video Game', 2500)
p3 = Produto('Nintendo', 'Video Game', 2000)
print(p1.valor) # acesso incorreto de um atributo de classe
print(Produto.imposto) #acesso correto 
print(p1.id)
print(p2.id)
print(p3.id)

# Atributo Dinâmico é um atributo de instância que pode ser criado em tempo de execução.
# Será exclusivo da instância que o criou.
# Não é comum usar

class Produto:

    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao 
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

p1 = Produto('Arroz', 'Mercearia', 5.99)
p1.peso = '5kg' # Atributo dinâmico, diferente dos atributos de instâncias
p2 = Produto('Ps5', 'Video Game', 5000)

print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}' )

print(p2.__dict__)