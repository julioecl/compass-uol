"""
Lendo arquivos CSV

Modo não muito bom para trabalhar:
with open('lutadores.csv') as arquivo:
    dados = arquivo.read()    
    print(dados)

reader -> permite que iteremos sobre as linhas do arquivo CSV como listas;
DictReader -> permite que iteremos sobre as linhas do arquivo csv como OrderedDicts
    
"""

# Reader

from csv import reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo) 
    next(leitor_csv) # pula o cabeçalho  
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')

# DictReader (usa virgula como padrão)

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)     
    for linha in leitor_csv:
        # Cada linha é um OrderedDicts
        print(f'{linha["Nome"]} nasceu no(a)(s) {linha["País"]} e mede {linha["Altura (em cm)"]} centímetros')

from csv import DictReader

# DictReader (com outro separador ';')

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=';')  # delimitador conforme arquivo.   
    for linha in leitor_csv:
        # Cada linha é um OrderedDicts
        print(f'{linha["Nome"]} nasceu no(a)(s) {linha["País"]} e mede {linha["Altura (em cm)"]} centímetros')