from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql.functions import sum as _sum

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# READ SILVER

df = spark.read.parquet("s3://de-project-lake-eu/silver/orders/")

# 🔥 BUSINESS AGGREGATION

df_gold = df.groupBy("country", "order_date").agg(_sum("amount").alias("total_sales"))

# WRITE GOLD

df_gold.write.mode("overwrite").parquet("s3://de-project-lake-eu/gold/sales/")
