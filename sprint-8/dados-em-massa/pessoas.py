import random
import time
import names

random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux=[]
dados=[]

for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

for i in range(0,qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

with open('./dados-em-massa/nomes_aleatorios.txt', 'w') as txtfile:
    [txtfile.write(dado + '\n') for dado in dados]