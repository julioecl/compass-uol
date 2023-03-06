"""
POO - Método super()

O método super() se refere à super classe.
"""

class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie
    
    def faz_som(self, som):
        print(f'O {self.__nome} faz {som}')

class Gato(Animal):

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie) modo não muito usual.
        super().__init__(nome, especie) 
        super().faz_som('MIAU') # pode-se acessar o método da classe pai.
        self.__raca = raca

felix = Gato('Felix', 'Felino', 'Angorá')
felix.faz_som('miau')