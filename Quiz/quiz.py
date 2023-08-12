import time

from DB import Db_Con
import mysql.connector
from datetime import date


# Function to retrieve and display a set of quiz questions
def display_question():
    connection = Db_Con.db_connector()

    if not connection:
        print("Failed to establish the database connection.")
        return
    try:
        with connection.cursor() as cursor:
            cursor.execute("USE python_TP_DB")
            cursor.execute("SELECT * FROM questions ORDER BY RAND() LIMIT 5")
            result = cursor.fetchall()
        if not result:
            print("NO Data FOUND!!")
            return 0
        else:
            return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")


# Function to display a message and score after completing the quiz
def display_score_message(total_correct):
    print("Quiz completed!")
    print(f"Your score: {total_correct}/5")
    percentage = total_correct * 20  # Since each correct answer is worth 20% of the total score

    if total_correct == 0 or total_correct == 1 or total_correct == 2:
        print("Please try again!")
    elif total_correct == 3:
        print("Good job!")
    elif total_correct == 4:
        print("Excellent work!")
    elif total_correct == 5:
        print("You are a genius!")
    print(f"Percentage: {percentage}%")
    time.sleep(4)


# Function to upload the user's quiz score to the database
def upload_score(user_id, score):
    connection = Db_Con.db_connector()

    if not connection:
        print("Failed to establish the database connection.")
        return

    try:
        with connection.cursor() as cursor:
            cursor.execute("USE python_TP_DB")

            # Get the current date
            current_date = date.today()

            # Insert the user's quiz score into the quiz_results table
            query = "INSERT INTO quiz_results (user_id, score, date) VALUES (%s, %s, %s)"
            values = (user_id, score, current_date)
            cursor.execute(query, values)

            connection.commit()
            print("Score uploaded successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()  # Rollback the changes on error


# Function to retrieve quiz history for a specific user
def get_quiz_history(user_id):
    connection = Db_Con.db_connector()

    if not connection:
        print("Failed to establish the database connection.")
        return []

    try:
        with connection.cursor() as cursor:
            cursor.execute("USE python_TP_DB")
            cursor.execute("SELECT * FROM quiz_results WHERE user_id = %s", (user_id,))
            quiz_history = cursor.fetchall()
            return quiz_history

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []

# Function to get the highest and lowest quiz scores from a list of scores
def get_high_low_score(scores):
    min_score = None
    max_score = None
    for score in scores:
        if min_score is None or max_score is None:
            min_score = score
            max_score = score
        if min_score > score:
            min_score = score
        if max_score < score:
            max_score = score
    return min_score, max_score

