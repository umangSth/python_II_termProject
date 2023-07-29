import mysql

from DB import Db_Con


def user_login(username):
    # Establishing the database connection
    connection = Db_Con.db_connector()

    if not connection:
        print("Failed to establish the database connection.")
        return
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


def user_password_chk(username, password):
    # Establishing the database connection
    connection = Db_Con.db_connector()

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
                    return 1
                    # --->>> code for what we should do after successful login
                else:
                    return -1

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        connection.close()
