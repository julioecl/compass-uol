-- E8
-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), 
-- e que estas vendas estejam com o status concluída. 
-- As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

WITH tabela_vendas_concluidas as (
	SELECT	
		vendedor.cdvdd,
		vendedor.nmvdd,
		count(*) as vendas_concluidas 
	from tbvendas as vendas
	left join tbvendedor as vendedor
		on vendas.cdvdd = vendedor.cdvdd 
	WHERE vendas.status = 'Concluído'
	group by vendedor.cdvdd
)

SELECT 
	cdvdd,
	nmvdd	
from tabela_vendas_concluidas
where vendas_concluidas = (select max(vendas_concluidas) from tabela_vendas_concluidas)

-- E9
-- Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, 
-- e que estas vendas estejam com o status concluída. 
-- As colunas presentes no resultado devem ser cdpro e nmpro.

with tabela_vendas_concluidas as (
	SELECT 
		cdpro,
		nmpro,
		SUM(qtd) as soma_vendida 
	FROM tbvendas	
	where status = 'Concluído' and dtven BETWEEN '2014-02-03' and '2018-02-02'
	group by cdpro
)

SELECT
	cdpro,
	nmpro
FROM tabela_vendas_concluidas
WHERE soma_vendida = (select max(soma_vendida) from tabela_vendas_concluidas)

-- E10
-- A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. 
-- O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor.
-- Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.
-- As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao.
-- O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

WITH tabela_vendas_e_comissao as (
	SELECT	
		vendedor.nmvdd  as vendedor,		
		sum(vendas.qtd*vendas.vrunt) as valor_total_vendas,		
		round((round((vendedor.perccomissao),2)/100 * (sum(vendas.qtd*vendas.vrunt))),2) as comissao		
	from tbvendas as vendas
	left join tbvendedor as vendedor
		on vendas.cdvdd = vendedor.cdvdd	
	WHERE vendas.status = 'Concluído'
	group by vendedor.cdvdd
)

SELECT 
	vendedor,	
	valor_total_vendas,	
	comissao
from tabela_vendas_e_comissao
order by comissao DESC 

-- E11
-- Apresente a query para listar o código e nome cliente com maior gasto na loja.
-- As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

WITH gasto_por_cliente as (
	SELECT 
		cdcli,
		nmcli,
		sum(qtd*vrunt) as gasto
	FROM tbvendas 
	where status = 'Concluído'
	GROUP by cdcli
)

SELECT 
	cdcli,
	nmcli,
	gasto
from gasto_por_cliente
WHERE gasto = (select max(gasto) from gasto_por_cliente)

-- E12
-- Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). 
-- As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
-- Observação: Apenas vendas com status concluído.

WITH tabela_dependentes as (
	SELECT
		dependente.cddep,
		dependente.nmdep,
		dependente.dtnasc,
		sum(vendas.qtd*vendas.vrunt) as valor_total_vendas
	from tbdependente as dependente	
	left join tbvendedor as vendedor
		on dependente.cdvdd = vendedor.cdvdd
	left join tbvendas as vendas
		on vendedor.cdvdd = vendas.cdvdd 
	WHERE vendas.status = 'Concluído'
	group by dependente.cddep 
)

SELECT 
	cddep,
	nmdep,
	dtnasc,
	valor_total_vendas
from tabela_dependentes
WHERE valor_total_vendas = (select min(valor_total_vendas) from tabela_dependentes)

-- E13
-- Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).
-- As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

WITH produtos_mais_vendidos as (
	SELECT
		cdpro,
		nmcanalvendas,
		nmpro,
		SUM(qtd) as quantidade_vendas
	from tbvendas
	where status = 'Concluído' and (nmcanalvendas = 'Matriz' or nmcanalvendas = 'Ecommerce')
	group by nmpro, nmcanalvendas 	
)

SELECT 
	cdpro,
	nmcanalvendas,
	nmpro,
	quantidade_vendas
from produtos_mais_vendidos
order by quantidade_vendas
LIMIT 10

-- E14
-- Apresente a query para listar o gasto médio por estado da federação. 
-- As colunas presentes no resultado devem ser estado e gastomedio. 
-- Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente. 
-- Observação: Apenas vendas com status concluído.

WITH gasto_por_estado as (
	select
		estado,
		count(qtd) as total_vendas,
		ROUND(sum(qtd*vrunt),2) as gasto_total
	from tbvendas
	where status = 'Concluído'
	GROUP by estado	
)

SELECT 
	estado,
	ROUND((gasto_total/total_vendas),2) as gastomedio
from gasto_por_estado
order by gastomedio DESC 

-- E15
-- Apresente a query para listar os códigos das vendas identificadas como deletadas. 
-- Apresente o resultado em ordem crescente.
	
select
	cdven
from tbvendas
WHERE deletado is TRUE 

-- E16
-- Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. 
-- As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. 
-- Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. 
-- Ordene os resultados pelo estado (1º) e nome do produto (2º).
-- Obs: Somente vendas concluídas.

WITH qtde_por_estado as (
	select
		estado,
		nmpro,
		round(round(sum(qtd),4)/round(count(qtd),4),4) as quantidade_media
	from tbvendas
	where status = 'Concluído'
	GROUP by estado, nmpro	
)

SELECT 
	estado,
	nmpro,
	quantidade_media
from qtde_por_estado
order by estado, nmpro