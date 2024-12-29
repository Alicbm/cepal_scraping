def map_pandas_to_mysql(pandas_type):
    if pandas_type == 'int64':
        return 'INT'
    elif pandas_type == 'float64':
        return 'DECIMAL(10, 3)'
    elif pandas_type == 'object':
        return 'VARCHAR(255)'
    elif pandas_type == 'datetime64[ns]':
        return 'DATETIME'
    else:
        return 'TEXT'