"""
POO - Objetos

São instâncias da classe.
"""

class Lampada:
    def __init__(self, voltagem, luminosidade, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada
    
    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

lamp1 = Lampada(100, 60, 'branca')

lamp1.ligar_desligar()

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')