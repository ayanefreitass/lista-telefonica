import mysql.connector
from mysql.connector import errors
from datetime import datetime
class BD:
    _connection = None

    def connect(self):
        try:
            if self._connection is not None:
                return self._connection
            else:
                self._connection = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password="",
                database="contato"
                    
                )
                return self._connection
        except mysql.connection.errors.ProgrammingError as e:
            print("Error:", e)
            return{"Error:", e}
        
    def close(self):
        self._connection.close()
        self._connection = None
