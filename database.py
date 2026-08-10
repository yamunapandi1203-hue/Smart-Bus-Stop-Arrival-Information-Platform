import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1607",
        database="smartbus"
    )

    return connection


def test_connection():

    try:
        connection = get_connection()

        if connection.is_connected():
            print("MySQL connected successfully!")

        connection.close()

    except mysql.connector.Error as error:
        print("MySQL connection error:", error)


if __name__ == "__main__":
    test_connection()