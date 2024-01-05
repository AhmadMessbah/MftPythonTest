import mysql.connector
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from Ver3.controller.person_controller import PersonController


class PersonView:
    def __init__(self):
        self.controller = PersonController()
        win = Tk()
        win.geometry("550x280")
        win.title("Person Profile")

        # Id
        Label(win, text="Id").place(x=20, y=20)
        self.id = IntVar()
        Entry(win, textvariable=self.id, state="readonly").place(x=100, y=20)

        # Name
        Label(win, text="Name").place(x=20, y=60)
        self.name = StringVar()
        Entry(win, textvariable=self.name).place(x=100, y=60)

        # Family
        Label(win, text="Family").place(x=20, y=100)
        self.family = StringVar()
        Entry(win, textvariable=self.family).place(x=100, y=100)

        table = ttk.Treeview(win, columns=("a", "b", "c"), show="headings")
        table.heading("a", text="Id")
        table.heading("b", text="Name")
        table.heading("c", text="Family")

        table.column("a", width=60)
        table.column("b", width=100)
        table.column("c", width=100)
        table.place(x=250, y=20)

        table.bind("<ButtonRelease>", self.select_person)

        Button(win, text="Save", width=8, command=self.save_click).place(x=20, y=220)
        Button(win, text="Edit", width=8, command=self.edit_click).place(x=90, y=220)
        Button(win, text="Remove", width=8, command=self.remove_click).place(x=160, y=220)

        self.reset_form()

        win.mainloop()

    def save_click(self):

        msg.showinfo("Save", self.controller.save(self.name.get(), self.family.get()))
        self.reset_form()

    def edit_click(self):
        msg.showinfo("Edit", "Edit Done")
        self.reset_form()

    def remove_click(self):
        msg.showinfo("Remove", "Remove Done")
        self.reset_form()

    def reset_form(self):
        id.set(0)
        self.name.set("")
        self.family.set("")

        for item in self.table.get_children():
            self.table.delete(item)

        for person in self.controller.find_all():
            self.table.insert("", END, values=person)

    def select_person(self, event):
        person = self.table.item(self.table.focus())["values"]
        id.set(person[0])
        self.name.set(person[1])
        self.family.set(person[2])
