import mysql.connector
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg


def save_click():
    connection = mysql.connector.connect(host="localhost",user="root",password="root123", database="mft")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO PERSON_TBL (NAME,FAMILY) VALUES (%s,%s)", [name.get(), family.get()])
    connection.commit()
    msg.showinfo("Save", "Save Done")
    reset_form()

def edit_click():
    connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
    cursor = connection.cursor()
    cursor.execute("UPDATE PERSON_TBL SET NAME=%s,FAMILY=%s WHERE ID=%s", [name.get(), family.get(), id.get()])
    connection.commit()
    msg.showinfo("Edit", "Edit Done")
    reset_form()


def remove_click():
    connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM PERSON_TBL WHERE ID=%s", [id.get()])
    connection.commit()
    msg.showinfo("Remove", "Remove Done")
    reset_form()


def reset_form():
    id.set(0)
    name.set("")
    family.set("")

    for item in table.get_children():
        table.delete(item)

    connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PERSON_TBL")
    person_list = cursor.fetchall()

    for person in person_list:
        table.insert("", END, values=person)

def select_person(event):
    person = table.item(table.focus())["values"]
    id.set(person[0])
    name.set(person[1])
    family.set(person[2])

win = Tk()
win.geometry("550x280")
win.title("Person Profile")

# Id
Label(win, text="Id").place(x=20, y=20)
id = IntVar()
Entry(win, textvariable=id, state="readonly").place(x=100, y=20)

# Name
Label(win, text="Name").place(x=20, y=60)
name = StringVar()
Entry(win, textvariable=name).place(x=100, y=60)

# Family
Label(win, text="Family").place(x=20, y=100)
family = StringVar()
Entry(win, textvariable=family).place(x=100, y=100)

table = ttk.Treeview(win, columns=("a", "b", "c"), show="headings")
table.heading("a", text="Id")
table.heading("b", text="Name")
table.heading("c", text="Family")

table.column("a", width=60)
table.column("b", width=100)
table.column("c", width=100)
table.place(x=250, y=20)

table.bind("<ButtonRelease>", select_person)

Button(win, text="Save",width=8, command=save_click).place(x=20, y=220)
Button(win, text="Edit",width=8, command=edit_click).place(x=90, y=220)
Button(win, text="Remove",width=8, command=remove_click).place(x=160, y=220)

reset_form()

win.mainloop()
