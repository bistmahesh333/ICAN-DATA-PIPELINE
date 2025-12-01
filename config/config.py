# config/config.py

# JDBC driver path
JDBC_DRIVER_PATH = r"C:\libs\postgresql-42.5.6.jar"  # Modify to your actual JDBC driver location

# PostgreSQL connection details
JDBC_URL = "jdbc:postgresql://localhost:5432/ICAN"  # Modify if necessary
DB_USER = "postgres"
DB_PASSWORD = "password"

# JDBC Driver class
JDBC_DRIVER_CLASS = "org.postgresql.Driver"

# Optional: Query for loading data
QUERY = "(SELECT * FROM studentmgmt) AS student_data"  # Modify if necessary
