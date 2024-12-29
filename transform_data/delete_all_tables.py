import os
import mysql.connector
import openpyxl
import pandas as pd
from credentials import mysql_credentials
from rename_files_to_sql_tables import rename_files_to_sql_tables

try:
    connection = mysql.connector.connect(
        host=mysql_credentials.get("HOST"),
        user=mysql_credentials.get("USER"),
        password=mysql_credentials.get("PASSWORD"),
        database=mysql_credentials.get("DATABASE")
    )
    
    if connection.is_connected():
        print("Conexión exitosa a la base de datos")

    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()

    # Mostrar las tablas
    for table in tables:
        cursor.execute(f"DROP TABLE {table[0]}")

except mysql.connector.Error as e:
    print(f"Error conectando a la base de datos: {e}")