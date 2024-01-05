import mysql.connector

def save(name,family):
    connection = mysql.connector.connect(host="localhost",user="root",password="root123", database="mft")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO PERSON_TBL (NAME,FAMILY) VALUES (%s,%s)", [name, family])
    connection.commit()

def edit(id,name,family):
    connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
    cursor = connection.cursor()
    cursor.execute("UPDATE PERSON_TBL SET NAME=%s,FAMILY=%s WHERE ID=%s", [name, family, id])
    connection.commit()

def remove(id):
    connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM PERSON_TBL WHERE ID=%s", [id])
    connection.commit()

def find_all():
    connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PERSON_TBL")
    return cursor.fetchall()