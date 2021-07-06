from tkinter import *
import mysql.connector
from tkinter import messagebox
import datetime

hold = Tk()
hold.title("Log out")
hold.geometry("450x300")
hold.config(bg="white")
class LogOut:
    def __init__(self, master):
        self.name = Label(master, text="Enter your name and surname: ")
        self.name.place(x=130, y=20)
        self.name.config(bg="white")
        self.name_entry = Entry(master)
        self.name_entry.place(x=145, y=50)
        self.name_entry.config(bg="#9ccb3b")
        self.id_number = Label(master, text="Enter your ID number: ")
        self.id_number.place(x=155, y=100)
        self.id_number.config(bg="white")
        self.id_entry = Entry(master)
        self.id_entry.place(x=145, y=150)
        self.id_entry.config(bg="#9ccb3b")
        self.logbtn = Button(master, text="log in")
        self.logbtn.place(x=190, y=200)
        self.logbtn.config(bg="green", borderwidth="10")
        self.backbtn = Button(master, text="Back")
        self.backbtn.place(x=10, y=250)
        self.backbtn.config(bg="green", borderwidth="5")
    def backbtn(self):
        hold.destroy()
y = LogOut(hold)
hold.mainloop()
