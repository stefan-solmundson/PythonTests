import sqlite3


class Database:
    def __init__(self, filename, table_name='cpu_loads'):
        self.__filename = filename
        self.__table_name = table_name

    def __execute(self, query):
        """
        Convenience method that:
            opens a connection,
            retrieves a cursor,
            executes a query
            and then closes the connection.

        Should NOT be used for queries that retrieve data
        :param query:
        :return:
        """
        connection = sqlite3.connect(self.__filename)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    def create(self):
        """
        Method that creates a database and table
         if it does not exist already exist
        :return:
        """
        sql = f"CREATE TABLE IF NOT EXISTS {self.__table_name}(" \
              f"[id] INTEGER PRIMARY KEY," \
              f"[load] DECIMAL," \
              f"[created_at] DATETIME)"
        self.__execute(sql)

    def store(self, value):
        """
        Method that store a single data value into the table
        :param value:
        :return:
        """
        sql = f"INSERT INTO {self.__table_name} " \
              f"VALUES (null, {value}, datetime())"
        self.__execute(sql)