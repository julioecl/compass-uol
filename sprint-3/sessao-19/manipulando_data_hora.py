"""
Manipulando data e hora

Módulo integrado para trabalhar com data e hora: datetime


"""

import datetime

print(datetime.datetime.now()) # data e hora atual em Inglês

# (year, day, month, minute, second, microsecond)
print(repr(datetime.datetime.now())) 

inicio = datetime.datetime.now()

# alterar o horário para 16h 0min 0second 0microsecond

inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print('alterando datas', inicio)

# criar data/hora

evento = datetime.datetime(2019, 1, 1, 0)

print('evento', evento)

# receber dados do usuário e transformar em data

nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ') # recebe a data

nascimento = nascimento.split('/') # divide pela barra

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
# converte para formato em inglês

print(nascimento)

# acessando individualmente cada parte da data

import datetime

evento2 = datetime.datetime.now()
print(evento2.hour, 'Horas')
