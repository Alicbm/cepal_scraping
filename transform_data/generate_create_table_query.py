def generate_create_table_query(table_name, column_types):
    query = f"CREATE TABLE {table_name} (\n"
    columns = []
    for column, column_type in column_types.items():
        columns.append(f"  {column} {column_type}")
    query += ",\n".join(columns)
    query += "\n);"
    return query