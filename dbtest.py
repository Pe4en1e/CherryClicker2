import pymysql
from db_cfg.config import host,user,password,db_name



try:

    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('connected...')
    print('#' * 20)

    try:
        cursor = connection.cursor()
        cursor.execute('SHOW DATABASES;')
        print(cursor.fetchall())


    finally:
        connection.close()


except Exception as ex:
    print('Connection refused')
    print(ex)