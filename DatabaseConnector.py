from mysql import connector
from mysql.connector import Error


def get_instance():
    if DatabaseConnector.instance is None:
        DatabaseConnector()
    return DatabaseConnector.instance


class DatabaseConnector(object):
    instance = None
    connection = None
    cursor = None

    def __init__(self):
        if DatabaseConnector.instance is not None:
            raise Exception("this class is a singleton!")
        else:
            self.connect_database()
            if self.connection is not None:
                DatabaseConnector.instance = self
            else:
                print('Connection could not happen')
        print("init")

    def connect_cursor(self):
        self.cursor = self.connection.cursor()

    def connect_buffered_cursor(self):
        self.cursor = self.connection.cursor(buffered=True)

    def connect_database(self):
        if self.connection is None:
            try:
                connection = connector.connect(host='127.0.0.1', user='bot_fn_tracker', passwd='%G1965ob!Qz#',
                                               db="fortnite_tracker")
                if connection.is_connected():
                    self.connection = connection
                    db_info = connection.get_server_info()
                    print("Connected to MySQL Server version ", db_info)
                    cursor = connection.cursor()
                    cursor.execute("select database();")
                    record = cursor.fetchone()
                    print("You're connected to database: ", record)
                    cursor.close()
            except Error as e:
                print("Error while connecting to MySQL", e)
                print("Trying with vpn")
                try:
                    connection = connector.connect(host='127.0.0.1', user='bot_fn_tracker', passwd='%G1965ob!Qz',
                                                   db="fortnite_tracker")
                    if connection.is_connected():
                        self.connection = connection
                        db_info = connection.get_server_info()
                        print("Connected to MySQL Server version ", db_info)
                        cursor = connection.cursor()
                        cursor.execute("select database();")
                        record = cursor.fetchone()
                        print("You're connected to database: ", record)
                        cursor.close()
                except Error as e:
                    print("Error while connecting to MySQL", e)
                    print("Trying with vpn")

    def query(self, query, params):
        self.cursor.execute(query, params)

    def close_database(self):
        try:
            self.connection.close()
            print("Database closed !")
        except Error as e:
            print(f"DB is already closed (Error code) : {e}")

    @classmethod
    def get_instance(cls):
        if DatabaseConnector.instance is None:
            DatabaseConnector()
        return DatabaseConnector.instance
