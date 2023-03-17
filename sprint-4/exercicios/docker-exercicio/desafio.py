"""
1 - Construa uma imagem a partir de um arquivo de instruções (Dockerfile) que execute o código carguru.py. 
Após, execute um container a partir da imagem criada.
Registre aqui o conteúdo de seu arquivo Dockerfile e o comando utilizado para execução do container.

FROM python:3

WORKDIR /app

COPY . .

CMD ["python", "app/index.py"]

Comandos: 

Criar imagem -> docker build -t car-guru-docker .

Rodar -> docker run -it car-guru-docker

2 - É possível reutilizar containers? 
Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? 
Não sendo possível reutilizar, justifique sua resposta.

Sim, é possível. Para isso seguir os passos:

Verificar containers que foram executados:
docker ps -a
Pegar a id do container que foi parado e dar um start nele:
docker start <id>

3 - Agora vamos exercitar a criação de um container que permita receber inputs durante sua execução. Seguem as instruções.

-- Criar novo script Python que implementa o algoritmo a seguir:

1 - Receber uma string via input

2 - Gerar o hash  da string por meio do algoritmo SHA-1

3 - Imprimir o hash em tela, utilizando o método hexdigest

4 - Retornar ao passo 1

Script Python:

from hashlib import sha1

resposta = 'S'

while resposta == 'S':
    palavra = input('Digite uma palavra para que eu possa encriptografá-la: ')
    palavra_encripto = sha1(palavra.encode()).hexdigest()
    print(f"O hexadecimal equivalente a SHA1 é : {palavra_encripto}")
    resposta = input('Digite S para continuar: ').upper()    



Dockerfile:

FROM python:3

WORKDIR /app

COPY . .

CMD ["python", "app/index.py"]

Comandos:

Criar a imagem: docker build -t mascarar-dados .

Rodar o container: docker run -it mascarar-dados

Resultado:

Digite uma palavra para que eu possa encriptografá-la: Julio
O hexadecimal equivalente a SHA1 é : 6edf0ebd13a0ded74ce8a686d505087b9e503f4c
Digite S para continuar: S   
Digite uma palavra para que eu possa encriptografá-la: Legal
O hexadecimal equivalente a SHA1 é : 902c91d94e0fd512d0a7f41cf7f018ee6f01bf85
Digite S para continuar: N

"""