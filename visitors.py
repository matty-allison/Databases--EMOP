from tkinter import *
import mysql.connector
from tkinter import messagebox
import datetime

root =Tk()
root.title("Welcome to Lifechoices Visitor")
root.geometry("400x400")
root.config(bg="green")
class visit:
    def __init__(self, master):
        self.visitor = Label(master, text="Please enter your name: ")

w = visit(root)
root.mainloop()
