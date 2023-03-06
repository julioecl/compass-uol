"""
POO - Abstração e Encapsulamento

O grande objetivo da poo é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados do usuário.

"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1 
    
    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor    
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

conta1 = Conta('Geek', 150.00, 1500)
conta2 = Conta('Geek2', 300, 2000)

print(conta1._Conta__numero) # Jeito errado de acessar um atributo privado. Name Mangling
print(conta1.__dict__)
print(conta2.__dict__)

conta2.transferir(100, conta1)

print(conta1.__dict__)
print(conta2.__dict__)
