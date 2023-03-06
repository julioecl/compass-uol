"""
POO - Polimorfismo

Quando um método é reimplementado na classe filha, ele é sobrescrito (overridding)

"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError ('Será implementado na classe filha')
    
    def comer(self):
        print(f'{self.__nome} está comendo...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala au au')

class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

pluto = Cachorro('Pluto')
pluto.falar()
pluto.comer()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()