import os
import psycopg
from psycopg.rows import dict_row

class DatabaseConnection:
    def connect(self):
        try:
            # Retrieve database URL from environment variable or use localhost as a fallback
            db_url = os.getenv("DATABASE_URL", "postgresql://localhost/food_tracker")
            self.connection = psycopg.connect(db_url, row_factory=dict_row)
        except psycopg.OperationalError:
            raise Exception(f"Couldn't connect to the database at {db_url}! " \
                            "Make sure the database is running and accessible.")


    # This method seeds the database with the given SQL file.
    # It is used to set up the database so that is is ready for tests or application.
    def seed(self, sql_filename):
        self._check_connection()
        if not os.path.exists(sql_filename):
            raise Exception(f"File {sql_filename} does not exist")
        with self.connection.cursor() as cursor:
            cursor.execute(open(sql_filename, "r").read())
            self.connection.commit()

    # This method executes an SQL query on the database.
    
    def execute(self, query, params=None):
        self._check_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description is not None:
                result = cursor.fetchall()
            else:
                result = None
            self.connection.commit()
            return result

    CONNECTION_MESSAGE = '' \
        'DatabaseConnection.exec_params: Cannot run a SQL query as ' \
        'the connection to the database was never opened. Did you ' \
        'make sure to call first the method DatabaseConnection.connect` ' \
        'in your app.py file (or in your tests)?'

    # This checks that we're connected to the database.
    def _check_connection(self):
        if self.connection is None:
            raise Exception(self.CONNECTION_MESSAGE)
