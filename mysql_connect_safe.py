import mysql.connector
from password_utils import get_decrypted_password

def connect_to_mysql():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=get_decrypted_password(),
        database="password"
    )
    print("Connected to MySQL Successfully! ✅")
    conn.close()

if __name__ == "__main__":
    connect_to_mysql()