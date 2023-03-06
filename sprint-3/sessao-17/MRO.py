"""
POO - Method Resolution Order - MRO

Basicamente é quem será executado primeiro.

Formas de conferir a ordem da execução
    - __mro__ 
    - help
    - método mro()
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

pinguim = Pinguim('Flue')
print(pinguim.andar())
print(pinguim.nadar())
print(pinguim.cumprimentar())

print(Pinguim.mro())