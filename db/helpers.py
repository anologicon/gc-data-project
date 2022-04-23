from sqlalchemy import create_engine

def import_query(path: str) -> str:
    """
    Imports a query from a file and returns it as a string.
    """
    with open(path, 'r') as f:
        return f.read()

def create_mysql_connection():
    return create_engine('mysql+pymysql://root:root@localhost:3306/gc_data')


def execute_multiple_queries(query: str, connection: object) -> None:
    """
    Executes multiple queries on a connection.
    """
    for q in query.split(';'):
        if q.strip() != '':
            connection.execute(q)