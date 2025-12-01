# config/database_utils.py

from pyspark.sql import SparkSession

def get_spark_session():
    # Create a Spark session
    spark = SparkSession.builder \
        .appName("Postgres Connection Example") \
        .config("spark.jars", "file:///path/to/your/jdbc/driver/postgresql-42.5.6.jar") \
        .getOrCreate()
    return spark

def load_data_from_postgres(spark):
    # Define PostgreSQL JDBC URL and properties
    url = "jdbc:postgresql://localhost:5432/ICAN"
    properties = {
        "user": "postgres",
        "password": "password",
        "driver": "org.postgresql.Driver"
    }
    
    # Load the data into a DataFrame from PostgreSQL
    df = spark.read.jdbc(url=url, table="studentmgmt", properties=properties)
    return df
