# main.py
from pyspark.sql import SparkSession

# ----------------------------
# 1. Create Spark session
# ----------------------------
spark = SparkSession.builder \
    .appName("Read PostgreSQL tbl_courses") \
    .config("spark.jars", "C:/Program Files/PostgreSQL/17/postgresql-42.5.6.jar") \
    .getOrCreate()

# ----------------------------
# 2. PostgreSQL connection settings
# ----------------------------
jdbc_url = "jdbc:postgresql://localhost:5432/ICAN"  # Database name: ICAN
jdbc_properties = {
    "user": "postgres",
    "password": "password",
    "driver": "org.postgresql.Driver"
}

# ----------------------------
# 3. Table to read (with schema)
# ----------------------------
table_name = "studentmgmt.tbl_courses"  # schema.table_name

# ----------------------------
# 4. Read data into DataFrame
# ----------------------------
df_courses = spark.read.jdbc(
    url=jdbc_url,
    table=table_name,
    properties=jdbc_properties
)

# ----------------------------
# 5. Show data
# ----------------------------
df_courses.show(truncate=False)  # truncate=False shows full text

# ----------------------------
# 6. Stop Spark session
# ----------------------------
spark.stop()
