import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
import re

## @params: [JOB_NAME]

args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH', 'S3_TARGET_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']
df_movies = glueContext.create_dynamic_frame.from_options(
    "s3",
    {"paths": [source_file]},
    "csv",
    {"withHeader": True, "separator":"|"},
    )
df_movies = df_movies.drop("generoArtista", "personagem", "nomeArtista", "anoNascimento", "anoFalecimento", "profissao", "titulosMaisConhecidos")
df_movies = df_movies.filter(lambda row: re.search(r'\bWar\b', row['genero']))
df_movies = df_movies.toDF()
df_movies = df_movies.distinct()
df_movies = DynamicFrame.fromDF(df_movies, glueContext, "movies" )

glueContext.write_dynamic_frame.from_options(
    frame = df_movies,
    connection_type = "s3",
    connection_options = {"path": target_path},
    format = "parquet")   
job.commit()