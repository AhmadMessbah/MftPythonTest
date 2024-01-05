from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from Ver2.db_module import *
from Ver2.validation import *


def save_click():
    try:
        if (name_validator(name.get())) and name_validator(family.get()):
            save(name.get(), family.get())
            msg.showinfo("Save", "Save Done")
            reset_form()
    except Exception as e:
        msg.showerror("Error", e)

def edit_click():
    try:
        if name_validator(name.get()) and name_validator(family.get()):
            edit(id.get(), name.get(), family.get())
            msg.showinfo("Edit", "Edit Done")
            reset_form()
    except Exception as e:
        msg.showerror("Error", e)

def remove_click():
    try:
        remove(id.get())
        msg.showinfo("Remove", "Remove Done")
        reset_form()
    except Exception as e:
        msg.showerror("Error", e)

def reset_form():
    id.set(0)
    name.set("")
    family.set("")

    for item in table.get_children():
        table.delete(item)

    for person in find_all():
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

Button(win, text="Save", width=8, command=save_click).place(x=20, y=220)
Button(win, text="Edit", width=8, command=edit_click).place(x=90, y=220)
Button(win, text="Remove", width=8, command=remove_click).place(x=160, y=220)

reset_form()

win.mainloop()
