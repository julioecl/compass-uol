"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código
Também externder nossas classes.

OBS: Com a herança a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos
comuns a outras entidades?

Quando uma classe herda de outra classe, ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    - Super Classe:
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada:
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;

"""

class Passaro:  

    def __init__(self, nome, som):
        self.nome = nome  
        self.som = som        
    
    def imprime(self):
        print(self.nome)
        print('Voando...')
        print(f'{self.nome} emitindo som...')
        print(self.som) 

class Pardal(Passaro):
    def __init__(self, nome, som):
        super().__init__(nome, som)

pardal = Pardal('Pardal', 'Piu Piu')

pardal.imprime()

"""
Sobrescrita de método
Ocorre quando reescrevemos um método presente na super classe na classe filha.

"""
class Passaro:  

    def __init__(self, nome, som):
        self.nome = nome  
        self.som = som        
    
    def imprime(self):
        print(self.nome)
        print('Voando...')
        print(f'{self.nome} emitindo som...')
        print(self.som)  

class Pato(Passaro):
    def __init__(self, nome, som, bico):
        super().__init__(nome, som)
        self.bico = bico

    def imprime(self): # Sobrescrita de método.
        print(self.nome)
        print('Voando...')
        print(f'{self.nome} emitindo som... pelo seu bico {self.bico}')
        print(self.som)

pato = Pato('Pato', 'Quack Quack', 'comprido')
pato.imprime()