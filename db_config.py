import pymysql

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Harrylol3002!',
        database='consultorio_psicologia',
        cursorclass=pymysql.cursors.DictCursor
    )
