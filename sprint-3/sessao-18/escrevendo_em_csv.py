"""
Escrevendo em arquivos csv

# Writer (trabalha com listas)

writer() -> gera um objeto para que possamos escrever em um arquivo CSV.
writerow() -> escreve linha

'w' - write
'a' - 

"""

# Whiter (trabalha com listas)

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo) 
    filme = None 
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])

# DictWriter (trabalha com dicionários, chave e valor)

from csv import DictWriter

with open('filmes2.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None 
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao}) # Recebe chave e valor e precisam ser as mesmas do cabeçalho