
# src/main.py
# -------------------------
# Simple PySpark script to read PostgreSQL tables and join them
# Author: Your Name
# -------------------------

from pyspark.sql import SparkSession

# -------------------------
# STEP 1: Create Spark session
# -------------------------
# Spark session is the entry point for any Spark application.
spark = SparkSession.builder \
    .appName("ICAN ETL Example") \
    .config("spark.jars", "C:/Program Files/PostgreSQL/17/postgresql-42.5.6.jar") \
    .getOrCreate()

# -------------------------
# STEP 2: JDBC connection properties
# -------------------------
# Here we define the Postgres connection parameters.
# These will be used in each read operation from Postgres.
jdbc_url = "jdbc:postgresql://localhost:5432/ICAN_ETL"
properties = {
    "user": "postgres",
    "password": "password",
    "driver": "org.postgresql.Driver"
}

# -------------------------
# STEP 3: Read dimension tables
# -------------------------
# We read 'dim_student' and 'dim_course' from 'data_warehouse' schema.
dim_student = spark.read.jdbc(
    url=jdbc_url,
    table="data_warehouse.dim_student",
    properties=properties
)

dim_course = spark.read.jdbc(
    url=jdbc_url,
    table="data_warehouse.dim_course",
    properties=properties
)

# -------------------------
# STEP 4: Read fact table
# -------------------------
fact_enrollment = spark.read.jdbc(
    url=jdbc_url,
    table="data_warehouse.fact_enrollment",
    properties=properties
)

# -------------------------
# STEP 5: Join tables to create a student-course report
# -------------------------
# Joining fact table with dimension tables to get descriptive info
report_df = fact_enrollment \
    .join(dim_student, "student_id") \
    .join(dim_course, "course_id") \
    .select(
        "student_id",
        "first_name",
        "last_name",
        "course_name",
        "course_type",
        "enrollment_date",
        "grade"
    )

# -------------------------
# STEP 6: Show the final report
# -------------------------
# Display top rows in console
report_df.show(truncate=False)

# -------------------------
# STEP 7: Stop Spark session
# -------------------------
# Always stop the session to free resources
spark.stop()
