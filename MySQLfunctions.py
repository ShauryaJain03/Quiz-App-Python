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

def insert_response(id,user_responseList):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("show tables like %s",(id,))
            table_exists = cursor.fetchone()
            if table_exists:
                table_name = id
                for i in user_responseList:
                    data_list=i
                    placeholders = ', '.join(['%s'] * len(data_list))
                    query = f"INSERT INTO {table_name} VALUES ({placeholders})"
                    cursor.execute(query, data_list)
                    connection.commit()
            else:
                table_name = id
                create_query=f"CREATE TABLE {table_name} (question varchar(200) , difficulty varchar(15) ,choice integer, answer varchar(12) ,time decimal(20,17), hint varchar(200),code char(5))"
                cursor.execute(create_query)
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
