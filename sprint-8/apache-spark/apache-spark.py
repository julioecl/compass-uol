from pyspark.sql import SparkSession
from pyspark.sql import functions as Func
from pyspark.sql.functions import when, rand, element_at, floor, lit
from pyspark import SparkContext, SQLContext

spark = SparkSession \
    .builder \
    .master("local[*]")\
    .appName("Exercicio Intro") \
    .getOrCreate()

# 1 - Nesta etapa, adicione código para ler o arquivo nomes_aleatorios.txt através do comando spark.read.csv. 
# Carregue-o para dentro de um dataframe chamado df_nomes e, por fim, liste algumas linhas através do método show. 
# Exemplo: df_nomes.show(5)

df_nomes = spark.read.csv("./dados-em-massa/nomes_aleatorios.txt")
df_nomes.show(5)

# 2 - No Python, é possível acessar uma coluna de um objeto dataframe pelo atributo (por exemplo df_nomes.nome) ou por índice (df_nomes['nome']). 
# Enquanto a primeira forma é conveniente para a exploração de dados interativos, você deve usar o formato de índice, pois caso algum nome de coluna não esteja de acordo seu código irá falhar.
# Como não informamos no momento da leitura do arquivo, o Spark não identificou o Schema por padrão e definiu todas as colunas como string. Para ver o Schema, use o método df_nomes.printSchema().
# Nesta etapa, será necessário adicionar código para renomear a coluna para Nomes, imprimir o esquema e mostrar 10 linhas do dataframe.

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')
df_nomes.printSchema()
df_nomes.show(10)

# 3 - Ao dataframe (df_nomes), adicione nova coluna chamada Escolaridade e atribua para cada linha um dos três valores de forma aleatória: Fundamental, Medio ou Superior.
# Para esta etapa, evite usar funções de iteração, como por exemplo: for, while, entre outras. Dê preferência aos métodos oferecidos para próprio Spark.

df_nomes = df_nomes.withColumn('Escolaridade', when(rand() <= 0.33, 'Fundamental')
                                                       .when(rand() <= 0.66, 'Medio')
                                                       .otherwise('Superior'))
df_nomes.show(10)

# 4 - Ao dataframe (df_nomes), adicione nova coluna chamada Pais e atribua para cada linha o nome de um dos 13 países da América do Sul, de forma aleatória.
# Para esta etapa, evite usar funções de iteração, como por exemplo: for, while, entre outras. Dê preferência aos métodos oferecidos para próprio Spark.

paises = ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'Guiana Francesa', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela']

df_nomes = df_nomes.withColumn("Rand", floor(rand()*(len(paises))).cast("int"))
df_nomes = df_nomes.withColumn("Pais", element_at(lit(paises), df_nomes["Rand"] + 1))

df_nomes = df_nomes.drop("Rand")
df_nomes.show(10)

# 5 - Ao dataframe (df_nomes), adicione nova coluna chamada AnoNascimento e atribua para cada linha um valor de ano entre 1945 e 2010, de forma aleatória. 
# Para esta etapa, evite usar funções de iteração, como por exemplo: for, while, entre outras. Dê preferência aos métodos oferecidos para próprio Spark.

df_nomes = df_nomes.withColumn("rand_col", rand())
df_nomes = df_nomes.withColumn("AnoNascimento", when(df_nomes["rand_col"] < 0.65, floor(df_nomes["rand_col"] * 100) + 1945)
                                .otherwise(floor(df_nomes["rand_col"] * 100) + 1910))
df_nomes = df_nomes.drop("rand_col")
df_nomes.show(10)

# 6 - Usando o método select do dataframe (df_nomes), selecione as pessoas que nasceram neste século. 
# Armazene o resultado em outro dataframe chamado df_select e mostre 10 nomes deste.

df_select = df_nomes.select('*').where(Func.col('AnoNascimento') > 2000)
df_select.show(10)

# 7 - Usando Spark SQL repita o processo da Pergunta 6. 
# Lembre-se que, para trabalharmos com SparkSQL, precisamos registrar uma tabela temporária e depois executar o comando SQL. 
# Abaixo um exemplo de como executar comandos SQL com SparkSQL:

# df_nomes.createOrReplaceTempView ("pessoas")
# spark.sql("select * from pessoas").show()

df_nomes.createOrReplaceTempView("nomes")
spark.sql("select * from nomes where AnoNascimento > 2000").show(10)

# 8 Usando o método select do Dataframe df_nomes, 
# Conte o número de pessoas que são da geração Millennials (nascidos entre 1980 e 1994) no Dataset

millenials_count = df_nomes.filter((Func.col('AnoNascimento') >= 1980) & (Func.col('AnoNascimento') <= 1994)).count()
print('O número total de Millennials é:', millenials_count)

# 9 - Repita o processo da Pergunta 8 utilizando Spark SQL

df_nomes.createOrReplaceTempView("nomes")
spark.sql("select count(*) as Millennials from nomes where AnoNascimento between 1980 and 1994").show()

# 10 - Usando Spark SQL, obtenha a quantidade de pessoas de cada país para cada uma das gerações abaixo. Armazene o resultado em um novo dataframe e depois mostre todas as linhas em ordem crescente de Pais, Geração e Quantidade

# - Baby Boomers – nascidos entre 1944 e 1964;

# - Geração X – nascidos entre 1965 e 1979;4

# - Millennials (Geração Y) – nascidos entre 1980 e 1994;

# - Geração Z – nascidos entre 1995 e 2015.

df_nomes.createOrReplaceTempView("geracoes")
df_geracoes = spark.sql("SELECT *, CASE WHEN AnoNascimento BETWEEN 1944 and 1964 then 'Baby Boomers' WHEN AnoNascimento BETWEEN 1965 and 1979 then 'Geração X' WHEN AnoNascimento BETWEEN 1980 and 1994 then 'Millennials' WHEN AnoNascimento BETWEEN 1995 and 2015 then 'Geração Z' ELSE NULL END AS Geracao FROM geracoes")

df_geracoes.createOrReplaceTempView("resultado")
spark.sql("SELECT Pais, Geracao, count (*) as Quantidade FROM resultado GROUP BY Pais, Geracao ORDER BY Pais, Geracao").show(10)