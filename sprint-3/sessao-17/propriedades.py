"""
POO - Propriedades - Properties

getters - retornar o valor do atributo e setters alteram o valor do mesmo

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1 

    def get_numero(self): # getter -> transforma um valor privado em publico. 
        return self.__numero
    
    def set_titular(self, titular): # setter -> alteram o valor do atributo / Perigoso usar.
        self.__titular = titular
    
    def extrato(self):
        print(f'Saldo de {self.__saldo} do cliente {self.__titular}')
    
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

conta1 = Conta('Geek', 3000, 5000)
conta2 = Conta('Geek2', 2000, 4000)

conta1.extrato()
conta2.extrato()

"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1    

    @property # getter -> tornar atibutos públicos
    def numero(self):
        return self.__numero 

    @property
    def saldo(self):
        return self.__saldo    
    
    @property
    def limite(self):
        return self.__limite  

    @numero.setter # setter -> alterar dados
    def numero(self, novo_numero):
        self.__numero = novo_numero 

    def extrato(self):
        print(f'Saldo de {self.__saldo} do cliente {self.__titular}')
    
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

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

conta1 = Conta('Geek', 3000, 5000)
conta2 = Conta('Geek2', 2000, 4000)

print(conta1.numero)
conta2.extrato()

conta1.numero = 76543

print('Numero da conta1:', conta1.numero)
print('Valor total, saldo + limite da conta1', conta1.valor_total)

