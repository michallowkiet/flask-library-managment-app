from postgresql_connection import PostgreSQLConnection


class Author:
    def __init__(self, name: str, db_connection: PostgreSQLConnection):
        self.id = -1
        self.name = name
        self.db_connection = db_connection

    def save(self):
        query = "INSERT INTO author (name) VALUES (%s) RETURNING id"
        params = (self.name,)
        result = self.db_connection.execute_query(query, params)
        self.id = result[0][0]
