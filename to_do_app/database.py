import cx_Oracle

class OracleDB:
    def __init__(self, username: str, password: str, dsn: str):
        self.username = username
        self.password = password
        self.dsn = dsn
        self.connection = None

    def connect(self):
        try:
            self.connection = cx_Oracle.connect(user=self.username, password=self.password, dsn=self.dsn)
            print("Connected to Oracle Database")
        except cx_Oracle.Error as error:
            print("Error connecting to Oracle Database:", error)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from Oracle Database")

    def execute_query(self, query: str, params: tuple = None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except cx_Oracle.Error as error:
            print("Error executing query:", error)

    def execute_statement(self, statement: str, params: tuple = None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(statement, params)
            else:
                cursor.execute(statement)
            cursor.close()
            self.connection.commit()
        except cx_Oracle.Error as error:
            print("Error executing statement:", error)
