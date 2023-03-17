from hashlib import sha1

resposta = 'S'

while resposta == 'S':
    palavra = input('Digite uma palavra para que eu possa encriptografá-la: ')
    palavra_encripto = sha1(palavra.encode()).hexdigest()
    print(f"O hexadecimal equivalente a SHA1 é : {palavra_encripto}")
    resposta = input('Digite S para continuar: ').upper()    
