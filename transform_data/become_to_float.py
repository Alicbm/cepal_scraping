import pandas as pd
import re

def contiene_caracteres_especiales_o_letras(texto):
    # Expresión regular para buscar:
    # 1. Cualquier letra (mayúscula o minúscula).
    # 2. Cualquier carácter especial, pero excluyendo coma y punto.
    return bool(re.search(r'[a-zA-Z]|[^a-zA-Z0-9\s,.]', texto))

def become_to_float(column):
    first_element = column[0]

    if column.dtype == 'object' and not contiene_caracteres_especiales_o_letras(str(first_element)[:2]) and column.str.contains(',').any():
        return pd.to_numeric(column.str.replace(',', '.'), errors='coerce')
    return column


# data = pd.read_excel(/Índice de efectividad migratoria global (IEMG).xlsx")

# print("PRIMERA", data.dtypes)
# files = os.listdir("/mnt/c/Users/Alic Barandica/Documents/proyectos/cepal_scraping/files/demografia")
# print(len(files))

# data = data.apply(become_to_float)
# print("SEGUNDA", data.dtypes)

# print("DATOS", data.head(5))







# print(contiene_caracteres_especiales_o_letras("0-4"))