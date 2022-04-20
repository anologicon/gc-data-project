from sqlalchemy import create_engine

def importQuery(path: str) -> str:
    """
    Imports a query from a file and returns it as a string.
    """
    with open(path, 'r') as f:
        return f.read()

def createMysqlConnection():
    return create_engine('mysql+pymysql://root:root@localhost:3306/gc_data')


def executeMultipleQueries(query: str, connection: object) -> None:
    """
    Executes multiple queries on a connection.
    """
    for q in query.split(';'):
        if q.strip() != '':
            connection.execute(q)