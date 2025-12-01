# main.py
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# ----------------------------
# 1. Create Spark session
# ----------------------------
spark = SparkSession.builder \
    .appName("Create DataFrame from List") \
    .getOrCreate()

# ----------------------------
# 2. Sample data as a list of tuples
# ----------------------------
data = [
    (1, "Mahesh", "Spark is working"),
    (2, "Sita", "Learning PySpark"),
    (3, "Ram", "DataFrame example")
]

# ----------------------------
# 3. Define schema for DataFrame
# ----------------------------
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("message", StringType(), True)
])

# ----------------------------
# 4. Create DataFrame from list
# ----------------------------
df = spark.createDataFrame(data, schema)

# ----------------------------
# 5. Show data
# ----------------------------
df.show(truncate=False)

# ----------------------------
# 6. Stop Spark session
# ----------------------------
spark.stop()
