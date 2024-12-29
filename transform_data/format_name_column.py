import unicodedata

def format_name_column(name):
    # Eliminar tildes y otros caracteres especiales
    name = ''.join(
        (c if unicodedata.category(c) != 'Mn' else '') for c in unicodedata.normalize('NFD', name)
    )
    name = name.lower().replace(' ', '_')
    name = name.replace('(', '')
    name = name.replace(')', '')
    name = name.replace('-', '_')
    
    while '__' in name:
        name = name.replace('__', '_')
    return name[:64]