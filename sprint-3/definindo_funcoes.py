"""
Definindo funções
Funções são pequenas partes de códigos que realizam tarefas específicas;
Podem ou não receber entradas de dados e retornar um saída de dados;
Muito úteis para executar procedimentos similares por repetidas vezes;

Função built-in são funções integradas ao python.
print(), len(), min(),...

Exemplos de funções:
"""

# cores = ['verde', 'amarelo', 'azul', 'branco']

# print(cores)

# cores.append('roxo')

# print(cores)

"""
Como definir funções?

def nome_da_funcao(paramentros_de_entrada):
    bloco_da_funcao

nome_da_funcao -> sempre com letras minúsculas, se for composto, separado por underline: nome_da_funcao
parametros_de_entrada -> opicionais, podendo ter 0 ou mais de um, sempre separado por vírgula.
bloco_da_funcao -> funcionalidade do código.

"""
def diz_oi():
    print('Oi!')

diz_oi()