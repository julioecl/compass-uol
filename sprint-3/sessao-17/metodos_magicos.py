"""
Métodos mágicos são todos métodos que utilizam __metodo__ (dunder)

__repr__ / __str__ -> representação do objeto, não retorna endereço de memória que o objeto se encontra.

__len__ -> definir um comprimento para o objeto

__del__ -> apresenta uma msg ao deletar uma váriável

__add__ -> concatena informações, o que não é permitido sem esse método

__mul__ -> multiplicar algo várias vezes.

"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return self.titulo
    
    def __len__(self):
        return self.paginas
    
    # def __del__(self):
    #     print('Um objeto foi deletado')

    def __add__(self, outro):
        return f'{self} - {outro}'
    
    def __mul__(self, outro):        
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'

livro1 = Livro('Python Rocks', 'Geek University', 400)
livro2 = Livro('I.A. com Python', 'Geek University', 350)

print(len(livro1))
print(livro2)

print(livro1 + livro2)
print(livro1 * 3)