"""
Exercícios Parte 1 - 21
Implemente duas classes Pato e Pardal que herdem de uma classe Passaro a habilidade de voar e emitir som, porém, tanto Pato quanto Pardal devem emitir sons diferentes
(de maneira escrita) no console.

Imprima no console exatamente assim:

Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu
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
    def __init__(self, nome, som):
        super().__init__(nome, som)

class Pardal(Passaro):
    def __init__(self, nome, som):
        super().__init__(nome, som)


pato = Pato('Pato', 'Quack Quack')
pardal = Pardal('Pardal', 'Piu Piu')

pato.imprime()
pardal.imprime()
"""
Exercícios Parte 1 - 22
Crie uma classe chamada "Pessoa" com um atributo privado "nome" (representado como "__nome") e um atributo público "id". Adicione duas funções à classe, uma para definir o valor de "nome" e outra para obter o valor de "nome". Observe que o atributo "nome" deve ser privado e acessado somente através dessas funções.

Para testar seu código use:

pessoa = Pessoa(0) 
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
"""

class Pessoa:

    def __init__(self, nome):
        self.__nome = nome
        self.id = id
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome = value

pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
"""
Exercícios Parte 1 - 23
Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).

Utilize os valores abaixo para testar seu exercício:

x = 4 
y = 5
imprima:

Somando: 4+5 = 9
Subtraindo: 4-5 = -1
"""
class Calculo:
    
    def __init__(self, num1, num2):
        self.num1 = num1 
        self.num2 = num2
    
    def soma(self):
        return self.num1 + self.num2
    
    def subtracao(self):
        return self.num1 - self.num2
    
x = 4 
y = 5

teste = Calculo(x, y)
print(f'Somando {x}+{y} = {teste.soma()}')
print(f'Subtraindo {x}-{y} = {teste.subtracao()}')

"""

Exercícios Parte 1 - 24
Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha os métodos ordenacaoCrescente e ordenacaoDecrescente.

Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como listaBaguncada a lista [3,4,2,1,5] e instancie um outro objeto, decrescente dessa mesma classe com uma outra listaBaguncada sendo [9,7,6,8].

Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto, use o método

ordenacaoDecrescente.

Imprima o resultado da ordenação crescente e da ordenação decresce

[1, 2, 3, 4, 5] 
[9, 8, 7, 6]
"""
class Ordenadora:

    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada
    
    def ordenacaoCrescente(self):     
        return sorted(self.listaBaguncada )

    def ordenacaoDecrescente(self):             
        return sorted(self.listaBaguncada ,reverse=True)       

crescente = Ordenadora([3,4,2,1,5])
decrescente = Ordenadora([9,7,6,8])

print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())

"""
Exercícios Parte 1 - 25
Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade.

Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião sejam da cor “azul”.

Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.

Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:

“O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para “z” passageiros e é da cor “w”.

Sendo x, y, z e w cada um dos atributos da classe “Avião”.

Valores de entrada:

modelo BOIENG456: velocidade máxima 1500 km/h: capacidade para 400 passageiros: Cor Azul

modelo Embraer Praetor 600: velocidade máxima 863km/h: capacidade para 14 passageiros: Cor Azul

modelo Antonov An-2: velocidade máxima de 258 Km/h: capacidade para 12 passageiros: Cor Azul

"""
class Aviao:

    def __init__(self, modelo, velocidade_maxima, capacidade, cor='azul'):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = cor

    def imprime(self):
        print(f'O avião de modelo {self.modelo} possui uma velocidade máxima de {self.velocidade_maxima}, capacidade para {self.capacidade} passageiros e é da cor {self.cor}')


lista = [('BOIENG456', 1500, 400), ('Embraer Praetor 600', 863, 14), ('Antonov An-2', 258, 12)]

for aviao in lista:    
    aviao = Aviao(aviao[0], aviao[1], aviao[2])
    aviao.imprime()