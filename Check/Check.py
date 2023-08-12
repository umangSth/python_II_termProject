import re

import mysql.connector

from DB import Db_Con


# Function to check if a value is not empty
def Check_String(value):
    if value != "":
        return value
    else:
        return Check_String(input("Invalid input(Null), try again:"))


# Function to check if an email is valid using regex
def Check_Email(value):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    email = Check_String(value)
    if re.fullmatch(regex, email):
        return email
    else:
        return Check_Email(input("Invalid email, try Again:"))


# Function to check if a password is valid using regex
def Check_Password(value):
    regex = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')
    password = Check_String(value)
    if re.fullmatch(regex, password):
        return password
    else:
        print("Password must contain at least 8 characters and may include A-Z, a-z, 0-9, "
              "and special characters (@, #, $, %, ^, &, +, =)")
        return Check_Password(input("Invalid password, try Again:"))


# Function to check if a username is unique and not already in use
def Check_Username(username):
    username = Check_String(username)
    if not Is_Username_Unique(username):
        print("User name already exists. Please choose a different user name.")
        return Check_Username(input("Enter your unique user name: "))
    else:
        return username


# Function to check if a username is unique in the database
def Is_Username_Unique(username):
    try:
        connection = Db_Con.db_connector()
        with connection.cursor() as cursor:
            cursor.execute("USE python_TP_DB")
            cursor.execute("SELECT user_id FROM users WHERE user_name = %s", (username,))
            result = cursor.fetchone()
            return result is None  # If result is None, the username is unique
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False  # return false on error


# Function to validate user's answer input
def check_answer_input(user_answer):
    try:
        user_answer = int(user_answer)
        if 1 <= user_answer <= 4:
            return user_answer
        else:
            return check_answer_input(input("Invalid input. Please enter a number between 1 and 4."))
    except ValueError:
        return check_answer_input(input("Invalid input. Please enter a number between 1 and 4."))


# Function to check if user's answer is correct based on question id and answer
def is_answer_correct(q_id, user_answer):
    try:
        connection = Db_Con.db_connector()
        with connection.cursor() as cursor:
            cursor.execute("USE python_TP_DB")
            cursor.execute("SELECT * FROM correct_answers WHERE q_id = %s and answer = %s", (q_id, user_answer,))
            result = cursor.fetchone()
            return not (result is None)  # If result is None, the user answer is incorrect
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None  # None when error
