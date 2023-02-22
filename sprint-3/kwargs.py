"""
**kwargs

Exige a utilização de parâmetros nomeados e os transforma em dicionário.

Não são parâmetros obrigatórios.

Ao declarar um função, os parâmetros seguem esta ordem

- Parâmetros obrigatórios;
- *args (não obrigatórios);
- Parâmetros default (não obrigatórios);
- **kwargs (não obrigatórios);
"""

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul')


def cumprimento_especial (**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

"""
Caso precisar desempacotar segue a mesma lógica dor *args, mas com **<nome_do_dicionário>
OBS: Os nomes das chaves em um dicionário devem ser os mesmos dos parâmetros da função.
"""
def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostra_nome(**nomes))
