"""
Métodos de data e hora

timedelta() adiciona alguma parte do dia a outro dia.

now() e today(), temos o mesmo resultado, mas no now(), podemos especificar um timezone, o que não acontece no today().

time() zera a hora para meia noite

weekday() dia da semana
1 - monday
2 - tuesday
3 - wednesday
4 - thursday
5 - friday
6 - saturday
7 - sunday

strptime() - transforma a data em uma data datetime

nascimento = datetime.datetime.strptime('10/04/1988', '%d/%m/%Y') # data, e formato dessa data

print(nascimento)


timeit() - tempo "disso"

tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000) #str, quantidade de vezes

print(tempo)

"""
import datetime
from textblob import TextBlob
import timeit

hoje = datetime.datetime.now()
print(hoje.weekday())

# Formatando horas com srtftime()

hoje_formatado = hoje.strftime('%d/%m/%Y') # Y - Ano completo / y - ano abreviado

print(hoje_formatado)

# textblob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B'))} de {data.year}"
    # return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}" para traduzir para o português

hoje2 = datetime.datetime.today()

print(formata_data(hoje2))

# strptime

nascimento = datetime.datetime.strptime('10/04/1988', '%d/%m/%Y') # data, e formato dessa data

print(nascimento.date()) # ignora as horas

# timeit

tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

print(tempo)