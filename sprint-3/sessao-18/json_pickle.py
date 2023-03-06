"""
JSON e PICKLE

JSON trabalha com aspas duplas.

import json

ret = json.dumps(['produto', {'Ps4': ('2TB', 'Novo', '220V', 2300)}])

print(ret)

import json

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
    
    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-Lata')

print(felix.__dict__) # {'_Gato__nome': 'Felix', '_Gato__raca': 'Vira-Lata'}

ret = json.dumps(felix.__dict__)

print(ret) # {"_Gato__nome": "Felix", "_Gato__raca": "Vira-Lata"}

Integrando JSON e PICKLE

pip instal jsonpickle

"""

# Escrevendo um arquivo JSON a partir do arquivo PYTHON com PICKLE:

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
    
    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-Lata')

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

# Lendo um arquivo JSON -> decode

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
    
    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(ret.nome)
    print(ret.raca)