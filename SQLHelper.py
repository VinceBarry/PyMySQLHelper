import pymysql


def connect(*args, **kwargs):
    connection = pymysql.connect(*args, **kwargs)
    cur = connection.cursor()
    return SQLHelper(connection, cur)


class SQLHelper(object):
    delimiter = ","
    SQL_TABLE_NAME = []
    SQL_ROW_VALUE = []

    def __init__(self, connection, cur):
        self.connection = connection
        self.cur = cur

    def insert(self, table, **kwargs):
        print(kwargs)
        for key in kwargs:
            self.SQL_TABLE_NAME.append(key)
            self.SQL_ROW_VALUE.append("\'"+kwargs[key]+"\'")
        self.SQL_TABLE_NAME = self.delimiter.join(self.SQL_TABLE_NAME)
        self.SQL_ROW_VALUE = self.delimiter.join(self.SQL_ROW_VALUE)
        print(self.SQL_TABLE_NAME)
        sql = "INSERT INTO " + table + " ( " + self.SQL_TABLE_NAME + " ) VALUES ( " + self.SQL_ROW_VALUE + " );"
        print(sql)
        self.cur.execute(sql)

    def close(self):
        self.cur.close()
        self.connection.close()
