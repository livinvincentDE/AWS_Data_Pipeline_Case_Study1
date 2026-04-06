from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql.functions import col

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# READ

df = glueContext.create_dynamic_frame.from_catalog(
database="de_db",
table_name="raw"
).toDF()

# 🔍 DATA QUALITY CHECKS

# 1. Null check

df = df.filter(col("order_id").isNotNull())

# 2. Valid amount

df = df.filter(col("amount") > 0)

# 3. Remove duplicates

df = df.dropDuplicates(["order_id"])

# 4. Optional: schema validation

expected_cols = ["order_id", "customer_id", "amount", "country", "order_date"]
missing_cols = [c for c in expected_cols if c not in df.columns]

if len(missing_cols) > 0:
  raise Exception(f"Missing columns: {missing_cols}")

# WRITE CLEAN DATA

df.write.partitionBy("order_date").mode("append").parquet("s3://de-project-lake-eu/processed/orders/")
