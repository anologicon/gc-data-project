import os
import sqlalchemy
import sys

import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

sys.path.insert(0, os.getenv("GC_PATH"))

from db.helpers import import_query, create_mysql_connection, execute_multiple_queries

ACTUAL_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(ACTUAL_PATH)
QUERIES_DIR = os.path.join(ROOT_DIR, 'queries')

etl_queries = []

etl_queries.append(import_query(os.path.join(QUERIES_DIR, 'player_resume.sql')))
etl_queries.append(import_query(os.path.join(QUERIES_DIR, 'player_lobby.sql')))


engine = create_mysql_connection()

try:
    for query in etl_queries:
        execute_multiple_queries(query, engine)
    print('Successfully created tables')
except Exception as e:
    print(e)

