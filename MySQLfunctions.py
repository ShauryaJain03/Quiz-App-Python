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


def insert_response(response):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO user_responses (question, response, answer, time_taken, hint_taken) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, response)
            connection.commit()
            print("User response inserted into the database")
        except Error as e:
            print(f'Error inserting user response: {e}')
        finally:
            cursor.close()
            connection.close()
            print("MySQL connection closed")


