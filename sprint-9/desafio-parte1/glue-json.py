import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

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
    "json"
)
df_movies = Filter.apply(
    frame=df_movies,
    f=lambda x: x["Orcamento"] != 0 and x["Renda"] != 0
)

df_movies = df_movies.toDF()
df_movies = df_movies.withColumnRenamed("NotaMedia:","NotaMedia")
df_movies = df_movies.withColumn("LucroPorDolarInvestido", df_movies["Renda"] / df_movies["Orcamento"])
df_movies = DynamicFrame.fromDF(df_movies, glueContext, "movies" )

glueContext.write_dynamic_frame.from_options(
    frame = df_movies,
    connection_type = "s3",
    connection_options = {"path": target_path},
    format = "parquet")   
job.commit()