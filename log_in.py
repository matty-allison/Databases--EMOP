from tkinter import *
import mysql.connector
from tkinter import messagebox
import datetime

box = Tk()
box.title("Log in!")
box.config(bg="green")
box.geometry("450x300")
class log:
    def __init__(self, master):
        self.name = Label(master, text="Enter your name and surname: ")
        self.name.place(x=130, y=20)
        self.name.config(bg="green")
        self.name_entry = Entry(master)
        self.name_entry.place(x=145, y=50)
        self.name_entry.config(bg="#9ccb3b")
        self.id_number = Label(master, text="Enter your ID number: ")
        self.id_number.place(x=155, y=100)
        self.id_number.config(bg="green")
        self.id_entry = Entry(master)
        self.id_entry.place(x=145, y=150)
        self.id_entry.config(bg="#9ccb3b")
        self.logbtn = Button(master, text="log in")
        self.logbtn.place(x=180, y=200)
        self.logbtn.config(bg="#9ccb3b", borderwidth="10")



x = log(box)
box.mainloop()
