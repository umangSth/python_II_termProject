import mysql.connector  # importing mysql connector

# Establishing the connection to mySql server
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_TP_DB"
    )
except mysql.connector.Error as err:
    print(f"Error: {err}")

Tables = {
    'users': """
        CREATE TABLE users(
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            user_name VARCHAR(50) UNIQUE,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            email VARCHAR(50),
            password VARCHAR(50)
        )
    """,
    'questions': """
    CREATE TABLE questions(
            q_id INT AUTO_INCREMENT PRIMARY KEY,
            question VARCHAR(150),
            answer_1 VARCHAR(30),
            answer_2 VARCHAR(30),
            answer_3 VARCHAR(30),
            answer_4 VARCHAR(30)
        )
    """,
    'correct_answer': """
    CREATE TABLE correct_answers(
            ans_id INT AUTO_INCREMENT PRIMARY KEY,
            q_id INT,
            answer VARCHAR(30),
            FOREIGN KEY (q_id) REFERENCES questions(q_id)
        )            
    """,
    'quiz_results': """
      CREATE TABLE quiz_results(
            quiz_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            score INT,
            date DATE,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        ) 
    """
}


# Function to drop the existing database if it exists
def drop_database():
    try:
        with connection.cursor() as cursor:
            cursor.execute("DROP DATABASE IF EXISTS python_TP_DB")
        print("Dropped the existing database.")
    except mysql.connector.Error as err:
        print(f"Error while dropping the database: {err}")


# creating a new database
def create_database():
    try:
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE python_TP_DB")
            print("Database created successfully.")

        with connection.cursor() as cursor:
            cursor.execute("USE python_TP_DB")
            for table_name, table_query in Tables.items():
                cursor.execute(table_query)
                print(f"{table_name} table created successfully.")

        connection.commit()  # Commit the changes
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()  # Rollback the changes on error


# calling the function to create database and table
drop_database()
create_database()

# closing the connection to create_database()
connection.close()


