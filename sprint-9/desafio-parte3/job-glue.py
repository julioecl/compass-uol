import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
from pyspark.sql.functions import col, when, row_number
from pyspark.sql.window import Window

## @params: [JOB_NAME]

args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH_CSV', 'S3_INPUT_PATH_TMDB', 'S3_TARGET_PATH_FINAL', 'S3_TARGET_PATH_DIM_FILME', 'S3_TARGET_PATH_DIM_VALOR', 'S3_TARGET_PATH_DIM_TEMPO', 'S3_TARGET_PATH_DIM_IDIOMA', 'S3_TARGET_PATH_FACT'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
source_file_csv = args['S3_INPUT_PATH_CSV']
source_file_tmdb = args['S3_INPUT_PATH_TMDB']
target_path = args['S3_TARGET_PATH_FINAL']
target_path_dim_filme = args['S3_TARGET_PATH_DIM_FILME']
target_path_dim_valor = args['S3_TARGET_PATH_DIM_VALOR']
target_path_dim_tempo = args['S3_TARGET_PATH_DIM_TEMPO']
target_path_dim_idioma = args['S3_TARGET_PATH_DIM_IDIOMA']
target_path_fact = args['S3_TARGET_PATH_FACT']
df_movies_csv = glueContext.create_dynamic_frame.from_options(
    "s3",
    {"paths": [source_file_csv]},
    format = "parquet"
    )
df_movies_tmdb = glueContext.create_dynamic_frame.from_options(
    "s3",
    {"paths": [source_file_tmdb]},
    format = "parquet"
    )
    
df_movies_csv = df_movies_csv.toDF()
df_movies_tmdb = df_movies_tmdb.toDF()
df_movies = df_movies_csv.join(df_movies_tmdb, col("id") == col("ImdbId"), "inner")
df_movies = df_movies.withColumn("decada",
                                 when(col("anolancamento").cast("int").between(1900, 1909), "1900s")
                                 .when(col("anolancamento").cast("int").between(1910, 1919), "1910s")
                                 .when(col("anolancamento").cast("int").between(1920, 1929), "1920s")
                                 .when(col("anolancamento").cast("int").between(1930, 1939), "1930s")
                                 .when(col("anolancamento").cast("int").between(1940, 1949), "1940s")
                                 .when(col("anolancamento").cast("int").between(1950, 1959), "1950s")
                                 .when(col("anolancamento").cast("int").between(1960, 1969), "1960s")
                                 .when(col("anolancamento").cast("int").between(1970, 1979), "1970s")
                                 .when(col("anolancamento").cast("int").between(1980, 1989), "1980s")
                                 .when(col("anolancamento").cast("int").between(1990, 1999), "1990s")
                                 .when(col("anolancamento").cast("int").between(2000, 2009), "2000s")
                                 .when(col("anolancamento").cast("int").between(2010, 2019), "2010s")
                                 .when(col("anolancamento").cast("int").between(2020, 2029), "2020s")
                                 .otherwise(None))
df_movies = df_movies.drop("notamedia", "tituloOriginal", "tempoMinutos", "numeroVotos", "id", "DataLancamento", "Titulo", "notamedia#1", "anolancamento")                                 

window = Window.orderBy("tituloPrincipal")
dim_filme = df_movies.select("tituloPrincipal", "Popularidade", "genero")
dim_filme = dim_filme.withColumn("IdFilme", row_number().over(window))

window = Window.orderBy("ImdbId")
dim_valor = df_movies.select("ImdbId", "Orcamento", "Renda", "LucroPorDolarInvestido")
dim_valor = dim_valor.withColumn("IdValor", row_number().over(window))

window = Window.orderBy("decada")
dim_tempo = df_movies.select("decada")
dim_tempo = dim_tempo.distinct()
dim_tempo = dim_tempo.withColumn("IdTempo", row_number().over(window))

window = Window.orderBy("IdiomaOriginal")
dim_idioma = df_movies.select("IdiomaOriginal")
dim_idioma = dim_idioma.distinct()
dim_idioma = dim_idioma.withColumn("IdIdioma", row_number().over(window))

fato_lucro = df_movies.select(df_movies["ImdbId"].alias("Id"), df_movies["tituloPrincipal"].alias("Titulo"), "Popularidade", "Orcamento", "Renda", "LucroPorDolarInvestido", df_movies["decada"].alias("Decadas"), df_movies["IdiomaOriginal"].alias("Idioma"))
fato_lucro = fato_lucro.join(dim_filme, col("Titulo") == col("tituloPrincipal"), "left")
fato_lucro = fato_lucro.join(dim_valor, col("Id") == col("ImdbId"), "left")
fato_lucro = fato_lucro.join(dim_tempo, col("Decadas") == col("decada"), "left")
fato_lucro = fato_lucro.join(dim_idioma, col("Idioma") == col("IdiomaOriginal"), "left")
fato_lucro = fato_lucro.drop("decada", "IdiomaOriginal", "ImdbId", "tituloPrincipal")
dim_filme = dim_filme.drop("Id_dim_filme")
dim_valor = dim_valor.drop("Id_dim_valor")

dim_filme = DynamicFrame.fromDF(dim_filme, glueContext, "dim_filme")
dim_valor = DynamicFrame.fromDF(dim_valor, glueContext, "dim_valor")
dim_tempo = DynamicFrame.fromDF(dim_tempo, glueContext, "dim_tempo")
dim_idioma = DynamicFrame.fromDF(dim_idioma, glueContext, "dim_idioma")
fato_lucro = DynamicFrame.fromDF(fato_lucro, glueContext, "fato_lucro")
df_movies = DynamicFrame.fromDF(df_movies, glueContext, "df_movies")

dim_filme = dim_filme.repartition(1)
dim_valor = dim_valor.repartition(1)
dim_tempo = dim_tempo.repartition(1)
dim_idioma = dim_idioma.repartition(1)
fato_lucro = fato_lucro.repartition(1)

glueContext.write_dynamic_frame.from_options(
    frame = dim_filme,
    connection_type = "s3",
    connection_options = {"path": target_path_dim_filme},
    format = "parquet")
    
glueContext.write_dynamic_frame.from_options(
    frame = dim_valor,
    connection_type = "s3",
    connection_options = {"path": target_path_dim_valor},
    format = "parquet")

glueContext.write_dynamic_frame.from_options(
    frame = dim_tempo,
    connection_type = "s3",
    connection_options = {"path": target_path_dim_tempo},
    format = "parquet")

glueContext.write_dynamic_frame.from_options(
    frame = dim_idioma,
    connection_type = "s3",
    connection_options = {"path": target_path_dim_idioma},
    format = "parquet")
    
glueContext.write_dynamic_frame.from_options(
    frame = fato_lucro,
    connection_type = "s3",
    connection_options = {"path": target_path_fact},
    format = "parquet")

glueContext.write_dynamic_frame.from_options(
    frame = df_movies,
    connection_type = "s3",
    connection_options = {"path": target_path},
    format = "parquet")  

job.commit()