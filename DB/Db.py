import mysql.connector  # importing mysql connector

from Data import questions_Data as q
from Data import tables

try:
    # Establishing the connection to mySql server
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")


    # Function to drop the existing database if it exists
    def drop_database():
        try:
            with connection.cursor() as cursor:
                cursor.execute("DROP DATABASE IF EXISTS python_TP_DB")
            print("Dropped the existing database.")
        except mysql.connector.Error as err:
            print(f"Error while dropping the database: {err}")


    # Creating a new database and its tables
    def create_database():
        try:
            with connection.cursor() as cursor:
                cursor.execute("CREATE DATABASE python_TP_DB")
                print("Database created successfully.")

            with connection.cursor() as cursor:
                cursor.execute("USE python_TP_DB")
                for table_name, table_query in tables.Tables.items():
                    cursor.execute(table_query)
                    print(f"{table_name} table created successfully.")

            connection.commit()  # Commit the changes
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()  # Rollback the changes on error


    # Inserting question data into the questions table
    def insert_question_data():
        try:
            with connection.cursor() as cursor:
                cursor.execute('USE python_TP_DB')
                for question in q.questions_data:
                    query = "INSERT INTO questions (question, answer_1, answer_2, answer_3, answer_4) " \
                            "VALUES (%s, %s, %s, %s, %s)"
                    values = (question['question'], question['answer_1'], question['answer_2'],
                              question['answer_3'], question['answer_4'])
                    cursor.execute(query, values)
                connection.commit()
                print("Questions inserted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()  # Rollback the changes on error

    # Inserting correct answers into the correct_answers table
    def insert_correct_answer():
        try:
            with connection.cursor() as cursor:
                cursor.execute("USE python_TP_DB")
                for question in q.questions_data:
                    # Get the q_id of the question from the questions table
                    cursor.execute("SELECT q_id FROM questions WHERE question = %s", (question['question'],))
                    q_id = cursor.fetchone()[0]

                    # Insert the correct answer along with the q_id into the correct_answers table
                    query = "INSERT INTO correct_answers (q_id, answer) VALUES (%s, %s)"
                    values = (q_id, question['correct_answer'])
                    cursor.execute(query, values)
                connection.commit()
                print("Correct answers inserted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()  # Rollback the changes on error


    # calling the function to create database and table
    drop_database()
    create_database()
    insert_question_data()
    insert_correct_answer()
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Always close the connection, whether there was an error or not
    if 'connection' in locals():
        connection.close()
