import boto3
import datetime
import os

s3 = boto3.client('s3')

ano_atual = datetime.datetime.now().strftime('%Y')
mes_atual = datetime.datetime.now().strftime('%m')
dia_atual = datetime.datetime.now().strftime('%d')

arquivos = ['movies.csv', 'series.csv']

for arquivo in arquivos:    
    with open(arquivo, 'rb') as arq:              
        file_type = os.path.splitext(arquivo)[1][1:].upper()
        name_file = os.path.splitext(arquivo)[0].capitalize()        
        s3.put_object(Bucket='data-lake-julio', Key=f'Raw/Local/{file_type}/{name_file}/{ano_atual}/{mes_atual}/{dia_atual}/{arquivo}', Body=arq)