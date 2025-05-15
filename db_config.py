import pyodbc

def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=GILBERTO_G;'
        'DATABASE=UEFA_Champion_League;'
        'Trusted_Connection=yes;'
    )