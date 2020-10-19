import sqlite3


class Database:
    def __init__(self, filename, table_name='cpu_loads'):
        self.__filename = filename
        self.__table_name = table_name

    def __execute(self, query):
        """Convenience method that:
            opens a connection,
            retrieves a cursor,
            executes a query
            and then closes the connection.

        This method should NOT be used for queries that retrieve data

        :param query:
        :return:
        """
        connection = sqlite3.connect(self.__filename)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    def __retrieve(self, query):
        """Convenience method to retrieve data from the database

        :param query:
        :return:
        """
        connection = sqlite3.connect(self.__filename)
        cursor = connection.cursor()
        cursor.execute(query)
        rows=cursor.fetchall()  # [(12,23.4), (34, 23)...]
        count=0
        results = {}
        for row in rows:
            results[count] = dict(zip(
                [c[0] for c in cursor.description], row))
            count += 1
        connection.close()
        return results

    def create(self):
        """Method that creates a database and table (if the pair do not exist already exist)

        :return:
        """
        sql = f"CREATE TABLE IF NOT EXISTS {self.__table_name}(" \
              f"[id] INTEGER PRIMARY KEY," \
              f"[load] DECIMAL," \
              f"[created_at] DATETIME)"
        self.__execute(sql)

    def store(self, value):
        """Method that stores a single data value into the table

        :param value:
        :return:
        """
        sql = f"INSERT INTO {self.__table_name} " \
              f"VALUES (null, {value}, datetime())"
        self.__execute(sql)

    def get_last(self, quantity="10"):
        """Method that return the last "quantity" results

        :param quantity:
        :return:
        """
        try:
            if not quantity.isnumeric():
                quantity = 10
        except AttributeError:
            value = (abs(int(quantity)))
        else:
            value = (abs(int(quantity)))
        query = f"SELECT * FROM {self.__table_name} " \
                f"ORDER BY created_at DESC " \
                f"LIMIT {value}"
        return self.__retrieve(query)