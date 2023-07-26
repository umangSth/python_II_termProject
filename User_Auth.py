import mysql

import Db_Con


def user_login(username, password):
    # Establishing the database connection
    connection = Db_Con.db_connector()

    if not connection:
        print("Failed to establish the database connection.")
        return

    try:
        with connection.cursor() as cursor:
            cursor.execute("USE python_TP_DB")
            cursor.execute("SELECT * FROM users WHERE user_name = %s;", username)

            result = cursor.fetchone()
            if result:
                user_id, _, _, _, _, stored_password = result
                if password == stored_password:
                    print("Login Successful.")
                    # --->>> code for what we should do after successful login
                else:
                    print("Invalid Password, Try-again!!!")
                    return -1
            else:
                # User not found or wrong Credentials.
                # ---->>> code to redirect or function to ask sign up
                print("Invalid username or Password")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        connection.close()
