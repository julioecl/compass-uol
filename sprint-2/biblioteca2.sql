-- Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV. 
-- Utilizar o caractere ; (ponto e vírgula) como separador. 
-- Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo:

-- CodLivro
-- Titulo
-- CodAutor
-- NomeAutor
-- Valor
-- CodEditora
-- NomeEditora

SELECT 
	liv.cod as CodLivro,
	liv.titulo as Titulo,
	aut.codautor as CodAutor,
	aut.nome as NomeAutor,
	liv.valor as Valor,
	edt.codeditora as CodEditora,
	edt.nome as NomeEditora
from livro as liv
left join autor as aut
	on liv.autor = aut.codautor
left join editora as edt
	on liv.editora = edt.codeditora
ORDER by liv.valor DESC
limit 10

-- Exportar o resultado da query que obtém as 5 editoras com maior quantidade de livros na biblioteca para um arquivo CSV. 
-- Utilizar o caractere | (pipe) como separador.
-- Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo:

-- CodEditora
-- NomeEditora
-- QuantidadeLivros

SELECT 
	edt.codeditora as CodEditora,
	edt.nome as NomeEditora,
	COUNT(liv.editora) as QuantidadeLivros
from livro as liv
left join editora as edt
	on liv.editora = edt.codeditora
	group by editora 
ORDER by QuantidadeLivros DESC
limit 5