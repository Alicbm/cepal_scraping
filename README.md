# 🌎 Informe para América Latina y el Caribe 📊  

Este repositorio contiene el desarrollo de un informe dinámico que analiza datos de los países de América Latina y el Caribe en múltiples categorías y a lo largo del tiempo. El enfoque principal fue la automatización de procesos para facilitar la actualización y el análisis de los datos.  

## 🚀 Objetivo  
Automatizar la descarga, procesamiento y análisis de bases de datos de la **CEPAL**, integrando tecnologías como **Python**, **SQL** y **Power BI**, para crear un informe interactivo y eficiente.  

---

## 🛠️ Proceso  

1. **Automatización de la descarga de datos**  
   - Implementé un script en Python para descargar las bases de datos desde la página oficial de la **CEPAL**.  
   - Este proceso elimina la necesidad de descargas manuales al aplicar los filtros directamente desde el script, asegurando que el análisis esté siempre actualizado.  

2. **Procesamiento y creación de tablas en SQL**  
   - Utilicé **Pandas** para procesar los datos y validar tipos, incluso ajustando números almacenados como texto.  
   - Las tablas en SQL se crean dinámicamente, adaptándose a la estructura de cada conjunto de datos.  

3. **Integración con Power BI**  
   - Los datos en SQL se conectaron a **Power BI** para crear visualizaciones interactivas.  
   - Los gráficos dinámicos permiten filtrar la información por **año** y **país**, facilitando el análisis específico para cada economía.  

---

## 📊 Categorías de análisis  

El informe cubre diversas áreas clave, incluyendo:  
- 👨‍👩‍👧‍👦 **Indicadores poblacionales**  
- 💰 **Economía**  
- 🏢 **Mercado laboral**  
- 📉 **Pobreza y desigualdad**  

---

## 🌟 Resultados  

- Una herramienta interactiva que analiza los datos históricos y actuales de América Latina y el Caribe.  
- Un flujo de trabajo automatizado que permite actualizar el informe fácilmente al ejecutarse el script.  

---

## 📂 Estructura del repositorio  

    .gitignore
    backup.sql
    complete_function.py
    coordinates/
        countries_coodinates.xlsx
        create_coordinates.py
    files/
        all_files/
        demografia/
        economicos/
        social/
    informe.pbix
    module/
        __pycache__/
        index.py
        main_function.py
        rename_downloaded_file.py
    requirements.txt
    transform_data/
        __pycache__/
        become_to_float.py
        create_tables.py
        credentials.py
        delete_all_tables.py
        format_name_column.py
        generate_create_table_query.py
        insert_data_sql.py
        map_pandas_to_mysql.py
    venv/
        bin/


---

## 🛠️ Tecnologías utilizadas  

- **Python**  
  - Pandas  
  - Requests 
  - Selenium
  - mysql-connector-python
- **SQL**  
  - MySQL (para el almacenamiento de datos)  
- **Power BI**  

---

## 📧 Contacto  

Si tienes alguna pregunta o sugerencia sobre este proyecto, no dudes en contactarme. Estoy disponible para colaborar en proyectos relacionados con automatización, análisis de datos y visualización.  

**Autor:** Alic Barandica  
**LinkedIn:** [Alic Barandica](https://www.linkedin.com/in/alic-barandica/)  
**Correo:** abarandica1234@gmail.com  

---  

## 🏷️ Licencia  

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.  

---
