import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="pizzamakerdatabase"

)

mycursor = mydb.cursor()

def show_menu():
    mycursor.execute("SELECT * FROM pizza_menu")
    r = mycursor.fetchall()
    return r
