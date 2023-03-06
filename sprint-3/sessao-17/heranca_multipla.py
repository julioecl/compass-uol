"""
POO - Herança múltipla
É a possibilidade de uma classe herdar de várias classes.
Dessa forma a classe filha herda todos os artibutos e métodos de todas as classes herdadas.

OBS: A herança múltipla pode ser feita de duas maneiras:
    - Multiderivação direta:
    - Multiderivação indireta: 

OBS: Não importa o tipo da derivação. 
A classe que realizar a herança, herdará todos os atributos e métodos das super classes.


# Multiderivação direta:

class Base1:
    pass

class Base2:
    pass

class MultiDerivada(Base1, Base2):
    pass

# Multiderivação indireta:

class Base1:
    pass

class Base2(Base1): #Herda diretamente a Base1
    pass

class Base3(Base2): #Herda diretamente a Base2 e indiretamente a Base1
    pass

class MultiDerivadas(Base3): #Herda diretamente a Base3, mas indiretamente a Base2 e Base1
    pass
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'
    
class Terreste(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'
    
class Pinguim(Terreste, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terreste('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

pinguim = Pinguim('Flue')
print(pinguim.andar())
print(pinguim.nadar())
print(pinguim.cumprimentar()) # Method Resolution Order 

# Objeto é instância de...

print(isinstance(pinguim, Animal)) 
print(isinstance(pinguim, Aquatico))
print(isinstance(pinguim, Terreste))
print(isinstance(pinguim, Pinguim))
print(isinstance(pinguim, object))   # Por padrão, ao criar uma class, ela herda de object. 