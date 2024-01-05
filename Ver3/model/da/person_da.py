import mysql.connector

class PersonDa:
    def save(self,person):
        connection = mysql.connector.connect(host="localhost",user="root",password="root123", database="mft")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO PERSON_TBL (NAME,FAMILY) VALUES (%s,%s)", [person.name, person.family])
        connection.commit()

    def edit(self,person):
        connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
        cursor = connection.cursor()
        cursor.execute("UPDATE PERSON_TBL SET NAME=%s,FAMILY=%s WHERE ID=%s", [person.name, person.family, id])
        connection.commit()

    def remove(self,id):
        connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM PERSON_TBL WHERE ID=%s", [id])
        connection.commit()

    def find_all(self,):
        connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM PERSON_TBL")
        return cursor.fetchall()