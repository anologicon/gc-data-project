import os
import sqlalchemy
import sys
from db.helpers import importQuery, createMysqlConnection, executeMultipleQueries

ACTUAL_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(ACTUAL_PATH)
QUERIES_DIR = os.path.join(ROOT_DIR, 'queries')


query = importQuery(os.path.join(QUERIES_DIR, 'player_loby.sql'))

engine = createMysqlConnection()

try:
    executeMultipleQueries(query, engine)
    print('Successfully created tables')
except Exception as e:
    print(e)

