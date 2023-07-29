from DB import Db_Con
import mysql


def user_registration(user_info):
    # Establishing the database connection
    connection = Db_Con.db_connector()

    if not connection:
        print("Failed to establish the database connection.")
        return
    try:
        with connection.cursor() as cursor:
            cursor.execute("USE python_TP_DB")
            sql = "INSERT INTO users(user_name, first_name, last_name, email, password) value (%s, %s, %s, %s, %s)"
            values = (user_info['user_name'], user_info['first_name'], user_info['last_name'], user_info['email'],
                      user_info['password'])
            cursor.execute(sql, values)
        connection.commit()  # commit the changes
        print("User data inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()  # Rollback the changes on error
    finally:
        connection.close()
