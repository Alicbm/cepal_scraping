import re
import unicodedata

def rename_files_to_sql_tables(original_string):
    # Eliminar la extensión del archivo y convertir a minúsculas
    filename_without_extension = original_string.rsplit('.', 1)[0].lower()

    table_name = ''.join(
        (c if unicodedata.category(c) != 'Mn' else '') for c in unicodedata.normalize('NFD', filename_without_extension)
    )

    # Reemplazar los espacios por guiones bajos
    table_name = re.sub(r'\s+', '_', table_name)

    # Eliminar cualquier carácter no alfanumérico o guion bajo
    table_name = re.sub(r'[^\w_]', '', table_name)

    return table_name[:64]  # cantidad maximma de caracteres que soporta mysql para los nombres