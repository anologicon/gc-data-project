import pandas as pd
import os
from db.helpers import createMysqlConnection

ACTUAL_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(ACTUAL_PATH)
DATA_DIR = os.path.join(ROOT_DIR, 'data')
GC_RAW_DATA = os.path.join(DATA_DIR, 'gc_raw_data')


def getFilePathAndNames() -> list:
    csv_paths = []

    for dirname, dirnames, filenames in os.walk(GC_RAW_DATA):
        for filename in filenames:
            if filename.endswith('.csv'):
                file_path = os.path.join(dirname, filename)
                csv_paths.append({
                    'path': file_path,
                    'name': filename
                })
    return csv_paths

def parseTableName(table_name: str) -> str:
    return table_name[:-4]

def createTablesWithPandas():
    csv_paths = getFilePathAndNames()
    for csv_path in csv_paths:
        df = pd.read_csv(csv_path['path'])
        df.to_sql(parseTableName(csv_path['name']), con=createMysqlConnection(),
                  if_exists='replace', index=False)

try:
    createTablesWithPandas()
    print('Successfully created tables')
except Exception as e:
    print(e)
