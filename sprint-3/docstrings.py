"""
Documentando funções com Docsrings

Documentar partes importantes do código, para não precisar tentar lembrar a forma que o código funciona
Passar para outras pessoas o que essas partes fazem.

usando o comando help(nome_da_função) temos essas partes informadas na tela

"""

print(help(print))

"""
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
"""
def quadrado(n):
    """ Retorna o quadrado o número informado! """
    return n**2

print(quadrado.__doc__)
"""
print(nome_da_funcao.__doc__)

Retorna o quadrado o número informado! 

"""