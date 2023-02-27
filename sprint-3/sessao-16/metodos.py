"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto pode realizar no sistema
- Métodos são escritos com letras mínusculas e se composto, separados por _.

Existem dois tipo de métodos, de instância e de classe.
"""
# Método de instância:

class Lampada:

    def __init__ (self, cor, voltagem, luminosidade):
        self.__voltagem = voltagem # atributos de instância
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligada = False
    
class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao 
        self.__valor = valor
        Produto.contador = self.__id
    
    def desconto(self, porcentagem):
        return (self.__valor * (100 - porcentagem)) / 100

p1 = Produto('Playstation 4', 'Video Game', 2300)

print(p1.desconto(20)) # passando o valor 20 para a porcentagem


# Método de classes:

class Produto:

    contador = 0

    @classmethod
    def conta_produtos(cls):
        print(f'Temos {cls.contador} produto(s) no sistema')


    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao 
        self.__valor = valor
        Produto.contador = self.__id
    
    def desconto(self, porcentagem):
        return (self.__valor * (100 - porcentagem)) / 100

p1 = Produto('PS5', 'Video Game', 5000)

p1.conta_produtos()
"""
# Qual método usar?

Métodos de classe: acesso aos atributos da classe e não de instância (self) 
Métodos de instância: acesso aos atributos da instância (ex: dentro do constructor)

"""

