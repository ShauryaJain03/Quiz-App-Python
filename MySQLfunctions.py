import mysql.connector
from mysql.connector import Error
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='test',
            user='root',
            password='s1j1H3a45%$'
        )
        if connection.is_connected():
            print('Connected to MySQL database')
    except Error as e:
        print(f'Error connecting to MySQL database: {e}')
    return connection

def insert_response(user_responseList):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            table_name = 'testdata'
            for i in user_responseList:
                data_list=i
                placeholders = ', '.join(['%s'] * len(data_list))
                query = f"INSERT INTO {table_name} VALUES ({placeholders})"
                cursor.execute(query, data_list)
                connection.commit()
        except Error as e:
            print(f'Error inserting user response: {e}')
        finally:
            cursor.close()
            connection.close()
            print("MySQL connection closed")
