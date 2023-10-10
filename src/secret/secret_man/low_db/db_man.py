import mysql.connector
from mysql.connector import MySQLConnection

class db:
    def __init__(self, user: str, password: str, host: str, database: str) -> None:
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.cnx = None
    
    def __enter__(self) -> MySQLConnection:
        
        self.cnx = mysql.connector.connect(
                                user= self.user,
                                password= self.password,
                                host= self.host,
                                database= self.database                                
                            )
        return self.cnx

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.cnx:
            self.cnx.close()