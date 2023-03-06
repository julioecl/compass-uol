"""
Trabalhando com deltas de data e hora.

data_inicial = ...
data_final = ...

delta é o intervalo de tempo entre duas datas/horas

"""

import datetime

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2023, 8, 3, 0)

tempo_para_evento = aniversario - data_hoje

tempo_para_pagar = data_hoje + datetime.timedelta(days=3)

print('Days to Julius birthday party', tempo_para_evento)
print('Vencimento do boleto', tempo_para_pagar.date())