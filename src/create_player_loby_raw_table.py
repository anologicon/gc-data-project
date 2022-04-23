import os
import sqlalchemy
import sys
from db.helpers import import_query, create_mysql_connection, execute_multiple_queries

ACTUAL_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(ACTUAL_PATH)
QUERIES_DIR = os.path.join(ROOT_DIR, 'queries')


query = import_query(os.path.join(QUERIES_DIR, 'player_lobby.sql'))

engine = create_mysql_connection()

try:
    execute_multiple_queries(query, engine)
    print('Successfully created tables')
except Exception as e:
    print(e)

