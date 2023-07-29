import mysql.connector  # importing mysql connector


# Establishing the connection to mySql server
def db_connector():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_TP_DB"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
