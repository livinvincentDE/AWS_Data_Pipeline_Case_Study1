from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql.functions import col

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# READ BRONZE

df = glueContext.create_dynamic_frame.from_catalog(
database="de_db",
table_name="raw"
).toDF()

# 🔍 CLEANING

df = df.filter(col("order_id").isNotNull())
df = df.filter(col("amount") > 0)
df = df.dropDuplicates(["order_id"])

# WRITE SILVER

df.write.partitionBy("order_date").mode("append").parquet("s3://de-project-lake-eu/silver/orders/")
