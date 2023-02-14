-- E1

-- Apresente a query para listar todos os livros publicados após 2014. 
-- Ordenar pela coluna cod, em ordem crescente, as linhas.  
-- Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma

-- Resposta:

SELECT * 
from livro
WHERE publicacao >= '2015-01-01'
order by cod

-- E2
-- Apresente a query para listar os 10 livros mais caros. 
-- Ordenar as linhas pela coluna valor, em ordem decrescente. 
-- Atenção às colunas esperadas no resultado final:  titulo, valor.

SELECT 
	titulo,
	valor
from livro
order by valor desc
limit 10

-- E3
-- Apresente a query para listar as 5 editoras com mais livros na biblioteca.
-- O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
-- Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

SELECT	
	COUNT(*) as quantidade,
	edt.nome,	
	endr.estado,
	endr.cidade	
FROM livro as liv
left join editora as edt
	on liv.editora = edt.codeditora
left join endereco as endr
	on edt.endereco = endr.codendereco 
group by liv.editora  
order by quantidade desc
limit 5

-- E4
-- Apresente a query para listar a quantidade de livros publicada por cada autor. 
-- Ordenar as linhas pela coluna nome (autor), em ordem crescente. 
-- Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).


SELECT
	aut.nome,
	aut.codautor,
	aut.nascimento,
	count (liv.cod) as quantidade
from autor as aut
left join livro as liv
	on aut.codautor = liv.autor
group by aut.nome
order by aut.nome

-- E5
-- Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil.
-- Ordene o resultado pela coluna nome, em ordem crescente.

SELECT 
	aut.nome 
from livro as liv
left join autor as aut 
	on liv.autor = aut.codautor
left join editora as edt
	on liv.editora = edt.codeditora
left join endereco as endr
	on edt.endereco = endr.codendereco
where endr.estado <> 'RIO GRANDE DO SUL' and endr.estado <> 'PARANÁ'
order by aut.nome

-- E6
-- Apresente a query para listar o autor com maior número de livros publicados.
-- O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

WITH qtde_publicacoes as (
	SELECT 
		aut.codautor,
		aut.nome,
		count (publicacao) as quantidade_publicacoes
	from livro as liv
	left join autor as aut
		on liv.autor = aut.codautor
	GROUP by aut.nome
)

SELECT 
	codautor,
	nome,
	quantidade_publicacoes
from qtde_publicacoes
where quantidade_publicacoes = (select max(quantidade_publicacoes) from qtde_publicacoes)

-- E7
-- Apresente a query para listar o nome dos autores com nenhuma publicação. 
-- Apresentá-los em ordem crescente.

WITH qtde_publicacoes as (
	SELECT 
		aut.codautor,
		aut.nome,
		count (publicacao) as quantidade_publicacoes
	from autor as aut
	left join livro as liv
		on aut.codautor = liv.autor
	GROUP by aut.nome
	order by aut.nome
)	

SELECT 
	nome	
from qtde_publicacoes
where quantidade_publicacoes = 0