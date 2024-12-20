class Author:
    def __init__(self, name: str, id: int = -1):
        self.id = id
        self.name = name

    def save(self, db_connection):
        if self.id:
            query = "INSERT INTO author (name) VALUES (%s) RETURNING id"
            params = (self.name,)
            result = db_connection.execute_query(query, params)
            self.id = result

    def update(self, db_connection):
        if self.id:
            query = "UPDATE author SET name = %s WHERE id = %s"
            params = (self.name, self.id)
            db_connection.execute_query(query, params)

    def delete(self, db_connection):
        if self.id:
            query = "DELETE FROM author WHERE id = %s"
            params = (self.id,)
            print(params)
            db_connection.execute_query(query, params, is_delete=True)

    @staticmethod
    def find_by_author_name(
        name: str,
        db_connection,
    ):
        query = "SELECT * FROM author WHERE name LIKE %s || '%%'"
        result = db_connection.execute_query(query, (name,))
        if result:
            return result
        return None

    @staticmethod
    def find_by_id(id, db_connection):
        query = "SELECT * FROM author WHERE id = %s"
        result = db_connection.execute_query(query, (id,))

        if result:
            return Author(result[1], result[0])
        return None

    @staticmethod
    def all(db_connection):
        query = "SELECT * FROM author"
        result = db_connection.execute_query(query, ())
        if result:
            return result
        return None

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }
