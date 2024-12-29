import os
import time
import mysql.connector
import pandas as pd
from credentials import mysql_credentials
from become_to_float import become_to_float
from format_name_column import format_name_column
from map_pandas_to_mysql import map_pandas_to_mysql
from generate_create_table_query import generate_create_table_query
from rename_files_to_sql_tables import rename_files_to_sql_tables
from insert_data_sql import insertar_datos

RUTA = "/mnt/c/Users/Alic Barandica/Documents/proyectos/cepal_scraping/files/demografia"

# falta insertar los datos en las tablas

def create_tables():

  try:
    connection = mysql.connector.connect(
      host=mysql_credentials.get("HOST"),
      user=mysql_credentials.get("USER"),
      password=mysql_credentials.get("PASSWORD"),
      database=mysql_credentials.get("DATABASE")
    )

    if connection.is_connected():
      print("Conexión exitosa a la base de datos")

    files = os.listdir(RUTA)
    
    for new_name in files:
      data = pd.read_excel(f"{RUTA}/{new_name}")
      name = rename_files_to_sql_tables(new_name)

      # creacion de tablas
      df = data.apply(become_to_float)

      columnas_formateadas = [
        format_name_column(col) for col in df.columns]

      df.columns = columnas_formateadas

      # Mapeo de tipos de columnas
      mysql_types = {col: map_pandas_to_mysql(
        dtype) for col, dtype in df.dtypes.items()}

      # Generar la consulta SQL para crear la tabla
      create_table_query = generate_create_table_query(name, mysql_types)

      cursor = connection.cursor()
      cursor.execute(create_table_query)

      print("tabla creada", name)

      insertar_datos(df, name, columnas_formateadas, cursor, connection)

  except mysql.connector.Error as e:
      print(f"Error conectando a la base de datos: {e}")


if __name__ == "__main__":
  create_tables()
