"""
Armazene o arquivo actors.csv dentro de uma nova pasta, após isso crie 5 arquivos do tipo “txt” vazios (1 para cada exercício do desafio).

Em seguida para cada uma das tarefas da sequencia, leia o arquivo actors.csv utilizando Python como linguagem de programação e depois de obter as repostas necessárias armazene cada um dos resultados em um dos arquivos “txt” criados.

Pontos de Atenção:

Para desenvolvimento deste exercício, não deve ser utilizado as bibliotecas Pandas e NumPy e/ou outras bibliotecas e engines que utilizam de dataframes.

Todas as transformações que julgarem necessárias, devem ser feitas utilizando os scripts Python e nenhuma modificação deve ser feita no arquivo actors.csv

Para leitura do arquivo actors.csv, não deve ser utilizado o módulo csv nativo do Python.

Perguntas dessa tarefa
O ator/atriz com maior número de filmes e o respectivo número de filmes.

A média do número de filmes por ator.

O ator/atriz com a maior média por filme.

O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

A lista dos Atores ordenada por pagamento. Do mais bem pago para o menos bem pago

"""
with open('sprint-3/exercicios-trilha/desafio/actors.csv') as arquivo:
    next(arquivo)   
    lista_total = []

    for linha in arquivo.readlines():
        linha = linha.strip('\n')
        campos = []
        dentro_de_aspas = False
        campo_atual = ""

        for caractere in linha:
            if caractere == ',' and not dentro_de_aspas:
                campos.append(campo_atual)
                campo_atual = ""
            elif caractere == '"':
                dentro_de_aspas = not dentro_de_aspas
            else:
                campo_atual += caractere

        campos.append(campo_atual)
        lista_total.append(campos)
        
total_filmes = 0
mais_filmes = 0
maior_media = 0
lista_pagamentos = []

for listas in lista_total:
    pagamento = float(listas[1])
    numero_filmes = int(listas[2])    
    media_filmes = float(listas[3])
    lista_pagamentos.append(pagamento)                            
    total_filmes += numero_filmes        
    if numero_filmes > mais_filmes:
        mais_filmes = numero_filmes    
    if media_filmes > maior_media:
        maior_media = media_filmes

numero_atores = len(lista_total)
media_filmes = total_filmes/numero_atores 

index_filme = None
for i, dados_ator in enumerate(lista_total):
    if str(mais_filmes) in dados_ator:
        index_filme = i
        break   

ator_mais_filmes = lista_total[index_filme][0]

maior_media_str = ("{:.2f} ".format(maior_media))

index_media = None
for i, dados_ator in enumerate(lista_total):    
    if maior_media_str in dados_ator:
        index_media = i        
        break   

ator_maior_media = lista_total[index_media][0]
 
lista_filmes = []
for filmes in lista_total:
    lista_filmes.append(filmes[4])

contagem = {}

for filme in lista_filmes:
    if filme in contagem:
        contagem[filme] += 1        
    else:
        contagem[filme] = 1

mais_comum = None
max_contagem = 0

for item, cont in contagem.items():
    if cont > max_contagem:
        mais_comum = item
        max_contagem = cont

maiores_salarios = []
lista_pagamentos_ordenada = sorted(lista_pagamentos, reverse=True)
for item in lista_pagamentos_ordenada:
    salario = ("{:.2f} ".format(item))
    maiores_salarios.append(salario) 

mais_bem_pagos = []        

for salario in maiores_salarios:        
    for i, dados_ator in enumerate(lista_total):
        if salario in dados_ator:
            mais_bem_pagos.append(lista_total[i][0])
    
with open('sprint-3/exercicios-trilha/desafio/exercicio1.txt', 'w') as exercicio1:
    exercicio1.write(f'{ator_mais_filmes} é quem possui mais filmes, total de {mais_filmes} filmes')

with open('sprint-3/exercicios-trilha/desafio/exercicio2.txt', 'w') as exercicio2:
    exercicio2.write(f'A média de filmes por atores é {media_filmes}')

with open('sprint-3/exercicios-trilha/desafio/exercicio3.txt', 'w') as exercicio3:
    exercicio3.write(f'{ator_mais_filmes} é quem possui a maior média de filmes')

with open('sprint-3/exercicios-trilha/desafio/exercicio4.txt', 'w') as exercicio4:
    exercicio4.write(f'O filme mais comum na lista é: {mais_comum}, com {max_contagem} vezes.')

with open('sprint-3/exercicios-trilha/desafio/exercicio5.txt', 'w') as exercicio5:
    exercicio5.write(f'A lista com os atores/atrizes mais bem pagos, do maior para menor:\n {mais_bem_pagos}')