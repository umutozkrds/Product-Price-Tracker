import mysql.connector


def connection():
    conn = mysql.connector.Connect(
        host="localhost",
        user="root",
        password="",
        database="urun_otomasyon",
    )
    mycursor = conn.cursor()
    return conn, mycursor

conn, mycursor = connection()
