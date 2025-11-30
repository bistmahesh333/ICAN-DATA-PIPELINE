# main.py

from pyspark.sql import SparkSession
from pyspark.sql import Row

# Create a SparkSession
# setLogLevel("WARN") reduces verbose INFO logs
spark = SparkSession.builder \
    .appName("Simple Spark Example") \
    .getOrCreate()
spark.sparkContext.setLogLevel("WARN")  # Only WARN & ERROR logs

# Create some simple data
data = [
    Row(id=1, message="Hello Spark"),
    Row(id=2, message="This is working")
]

# Create a DataFrame
df = spark.createDataFrame(data)

# Show the DataFrame in console
df.show()

# Stop SparkSession
spark.stop()
