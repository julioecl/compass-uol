"""
Conhecendo o Pickle

A função de Pickle é realizar o seguinte processo:

Objeto Python -> Binarização

Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

OBS: Não é seguro trabalhar com arquivos Pickles de fontes desconhecidas.

Fazendo a escrita:

felix = Gato('Felix')

with open('animais.picke', 'wb') as arquivo:
    pickle(felix, arquivo)

Fazendo a leitura:

with open('animais.picke', 'rb') as arquivo:
    gato = pickle.load(arquivo)
    print(f'O gato chama-se {gato._Animal__nome}')
    gato.mia()

"""

import pickle

class Animal:

    def __init__(self, nome):
        self.nome = nome
    
    def comer(self):
        print(f'{self.__nome} está comendo')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self._Animal__nome} está miando')

felix = Gato('Felix')

with open('animais.picke', 'wb') as arquivo:
    pickle.dump(felix, arquivo)
    
# with open('animais.picke', 'rb') as arquivo:
#     gato = pickle.load(arquivo)
#     print(f'O gato chama-se {gato._Animal__nome}')
#     gato.mia()