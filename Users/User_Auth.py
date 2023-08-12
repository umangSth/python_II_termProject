import mysql

from DB import Db_Con

current_user = None


# Function to perform user login
def user_login(username):
    # Establishing the database connection
    connection = Db_Con.db_connector()
    if not connection:
        print("Failed to establish the database connection.")
        return
    global current_user  # Use the global variable
    try:
        with connection.cursor() as cursor:
            cursor.execute("USE python_TP_DB")
            cursor.execute("SELECT * FROM users WHERE user_name = %s;", (username,))

            result = cursor.fetchone()
            if not result:
                # User not found
                print("Invalid username")
                return 0

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        connection.close()


# Function to check the user's password
def user_password_chk(username, password):
    # Establishing the database connection
    connection = Db_Con.db_connector()
    global current_user
    if not connection:
        print("Failed to establish the database connection.")
        return

    try:
        with connection.cursor() as cursor:
            cursor.execute("USE python_TP_DB")
            cursor.execute("SELECT * FROM users WHERE user_name = %s;", (username,))

            result = cursor.fetchone()
            if result:
                user_id, _, _, _, _, stored_password = result
                if password == stored_password:
                    current_user = result
                    return 1  # Password match
                else:
                    return -1  # Incorrect password

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        connection.close()

# Function to retrieve the current user session
def session():
    return current_user
