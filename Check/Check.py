import re

import mysql.connector

from DB import Db_Con


def Check_String(value):
    if value != "":
        return value
    else:
        return Check_String(input("Invalid input(Null), try again:"))


def Check_Email(value):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    email = Check_String(value)
    if re.fullmatch(regex, email):
        return email
    else:
        return Check_Email(input("Invalid email, try Again:"))


def Check_Password(value):
    regex = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')
    password = Check_String(value)
    if re.fullmatch(regex, password):
        return password
    else:
        print("Password must contain at least 8 characters and may include A-Z, a-z, 0-9, "
              "and special characters (@, #, $, %, ^, &, +, =)")
        return Check_Password(input("Invalid password, try Again:"))


def Check_Username(username):
    username = Check_String(username)
    if not Is_Username_Unique(username):
        print("User name already exists. Please choose a different user name.")
        return Check_Username(input("Enter your unique user name: "))
    else:
        return username


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
