import os
import subprocess
import getpass
from .low_db.db_man import db
from mysql.connector import MySQLConnection, Error
from typing import List

class SecretManager:
    _user = 'db_python_user'
    _host= 'localhost'
    _database= 'providers'

    @staticmethod
    def _list_key(cnx: MySQLConnection) -> List[str] | None:
        curs = cnx.cursor()
        query = "SELECT provider FROM providers"
        
        try:
            curs.execute(query)
            rows = curs.fetchall()
            variables = [row[0] for row in rows]
            return variables
        
        except Error as err: 
            print(f'An error occured whil reading data: {err}')    
            return None

    @classmethod
    def list_all_keys(cls) -> None:
        with db(cls._user, os.getenv(cls._user), cls._host, cls._database) as cnx:
            return cls._list_key(cnx=cnx)

    @classmethod
    def get_key(cls, name: str) -> str:
        with db(cls._user, os.getenv(cls._user), cls._host, cls._database) as cnx:
            env_var = cls._list_key(cnx)
            val = os.getenv(name)
            
            base_message = f'{name.capitalize()} is not a valid name'
            message =''
            hint = f'Add {name} to the envitroment variables.'

            if name in env_var:
                return val
            
            if val is None:
                message = ', neither as a envriroment variable nor an api key'            
            if name not in env_var and val is not None:
                message += ' despite being a valid enviroment variable because it do not belongs to the api key list'
            if not env_var:
                message += ' and there are no api keys defined so far'
                hint = ''
            if len(env_var) == 1:
                message += f' also the only api key avaliable is {env_var[0]}'
            elif len(env_var) > 1: 
                message += f',use one of these instead \n{",".join(env_var)}'
            
            raise ValueError(base_message + message + '.\n' + hint)
                          
    @classmethod
    def set_key(cls, name: str, key: str) -> None:
        with db(cls._user, os.getenv(cls._user), cls._host, cls._database) as cnx:
            if name in cls._list_key(cnx=cnx):
                raise ValueError(f'{name.capitalize()} it\'s already listed')

            cursor = cnx.cursor()
            query = 'INSERT INTO providers (provider) VALUES (%s)'
            cursor.execute(query, (name,))
            cnx.commit()

        subprocess.run(['setx', f'{name}', f'{key}', '/M'])
        print('variable set')

    @classmethod
    def set_key_from_prompt(cls) -> None:
        cls.set_key(
            input('set the name of the variable '),
            getpass.getpass('set the value of the variable ')
        )
        print("succes!", end='\n\n')