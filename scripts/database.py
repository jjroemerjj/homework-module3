"""
This is module responsible for connection with SQL database

"""

from DBcm import SQLError
from DBcm import UseDatabase
from mysql.connector import IntegrityError


dbconfig = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Qwerty69.',
    'database': 'homework-module3'
    }


def get_players():
    with UseDatabase(dbconfig) as cursor:
        _SQL = """ select * from wisla_krakow_players"""
        cursor.execute(_SQL)
        while True:
            row=cursor.fetchone()
            if row is None:
                break
            yield row


def get_player_list() -> list:
    return [player for player in get_players()]





# player_list = [player for player in get_players()]
# [print(row) for row in player_list]