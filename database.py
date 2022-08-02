import mysql.connector

class database:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "cc15")
        self.cursor = self.conn.cursor()

    def closeDB(self):
        self.cursor.close()
        self.conn.close()

    def selectone(self, sqlString, sqlData):
        self.connect()

        self.cursor.execute(sqlString, sqlData)
        result = self.cursor.fetchone()

        self.closeDB()

        return result

    def select_all(self, sqlString):
        self.connect()

        self.cursor.execute(sqlString)
        result = self.cursor.fetchall()

        self.closeDB()

        return result

    def save(self, sqlString, sqlData):
        self.connect()

        self.cursor.execute(sqlString, sqlData)
        self.conn.commit()

        self.closeDB()