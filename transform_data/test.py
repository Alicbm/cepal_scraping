import mysql.connector
import pandas as pd
from credentials import mysql_credentials

try:
  connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="candiomedes175",
    database="pepe"
  )

  if connection.is_connected():
    print("Conexión exitosa a la base de datos")

  cursor = connection.cursor()

except mysql.connector.Error as e:
  print(f"Error conectando a la base de datos: {e}")

# archivo_excel = "/mnt/c/Users/Alic Barandica/Documents/proyectos/cepal_scraping/files/demografia/Distribución porcentual de la población según área geográfica y sexo..xlsx"  # Cambiar por la ruta de tu archivo Excel
# dataframe = pd.read_excel(archivo_excel)

# dataframe = dataframe.where(pd.notnull(dataframe), None)

# for index, row in dataframe.iterrows():
#     sql = """
#     INSERT INTO distribucion_porcentual_de_la_poblacion_segun_area_geografica_y_ (indicator, area_geografica, sexo_estandar, pais_estandar, anos_estandar, value, unit, notes_ids, source_id) 
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """

#     valores = (
#       row['indicator'], 
#       row['Área geográfica'], 
#       row['Sexo__ESTANDAR'], 
#       row['País__ESTANDAR'], 
#       row['Años__ESTANDAR'], 
#       row['value'], 
#       row['unit'], 
#       float(str(row['notes_ids']).replace(',', '.')) if pd.notnull(row['notes_ids']) else None,
#       row['source_id']
#     )

#     cursor.execute(sql, valores)

# connection.commit()

# cursor.close()
# connection.close()

# print("Datos insertados correctamente.")


# archivo_excel = "/mnt/c/Users/Alic Barandica/Documents/proyectos/cepal_scraping/files/demografia/Distribución porcentual de la población según área geográfica y sexo..xlsx"  # Cambiar por la ruta de tu archivo Excel
# dataframe = pd.read_excel(archivo_excel)

# print(dataframe.columns)

