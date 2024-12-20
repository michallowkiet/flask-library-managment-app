import os

import psycopg2
from dotenv import load_dotenv


class PostgreSQLConnection:
    def __init__(self):
        self._set_config()
        self.connect()

    def _set_config(self):
        load_dotenv()
        self._connection_config = {
            "host": os.environ.get("host"),
            "port": os.environ.get("port"),
            "database": os.environ.get("database"),
            "user": os.environ.get("user"),
            "password": os.environ.get("password"),
        }

    def connect(self):
        self.connection = psycopg2.connect(**self._connection_config)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params, is_delete=False):

        self.cursor.execute(query, params)
        self.cursor.rowcount
        self.connection.commit()
        if is_delete:
            return None
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()
