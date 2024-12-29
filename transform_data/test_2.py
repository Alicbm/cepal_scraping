import pandas as pd

def insertar_datos(dataframe, name_table, columns_sql, cursor, connection):
  dataframe = dataframe.where(pd.notnull(dataframe), None)

  columnas_str = ", ".join(columns_sql)  # Ejemplo: "col1, col2, col3"
  placeholders = ", ".join(["%s"] * len(columns_sql))

  for index, row in dataframe.iterrows():
      sql = f"""
      INSERT INTO {name_table} ({columnas_str}) 
      VALUES ({placeholders})
      """

      valores = tuple(
        row[col] if pd.notnull(row[col]) else None
        for col in columns_sql
      )

      cursor.execute(sql, valores)
  
  connection.commit()

  print(f"Datos insertados correctamente para la tabla {name_table}")

# insertar_datos(datalframe, "distribucion_porcentual_de_la_poblacion_segun_area_geografica_y_", ["indicator", "area_geografica", "sexo_estandar", "pais_estandar", "anos_estandar", "value", "unit", "notes_ids", "source_id"])
