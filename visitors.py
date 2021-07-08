#this window is used to register visitors for the day and keeps there time of signing in and out
from tkinter import *
import mysql.connector
from tkinter import messagebox
import datetime

root =Tk()
root.title("Welcome to Lifechoices Visitor")
root.geometry("450x620")
root.config(bg="white")
class visit:
    def __init__(self, master):
        self.name = Label(master, text="Please enter your name and surname: ")
        self.name.place(x=100, y=10)
        self.name.config(bg="white")
        self.name_entry = Entry(master)
        self.name_entry.place(x=135, y=50)
        self.name_entry.config(bg="#9ccb3b")
        self.ID = Label(master, text="Please enter your ID number: ")
        self.ID.place(x=120, y=100)
        self.ID.config(bg="white")
        self.ID_entry = Entry(master)
        self.ID_entry.place(x=135, y=150)
        self.ID_entry.config(bg="#9ccb3b")
        self.number = Label(master, text="Please enter your cell phone number: ")
        self.number.place(x=100, y=200)
        self.number.config(bg="white")
        self.no_entry = Entry(master)
        self.no_entry.place(x=135, y=250)
        self.no_entry.config(bg="#9ccb3b")
        self.kin = Label(master, text="Please enter your next of kin's information: ")
        self.kin.place(x=80, y=300)
        self.kin.config(bg="white", borderwidth="5")
        self.kin_name = Label(master, text="Name and Surname: ")
        self.kin_name.place(x=150, y=350)
        self.kin_name.config(bg="white")
        self.kinname_entry = Entry(master)
        self.kinname_entry.place(x=135, y=400)
        self.kinname_entry.config(bg="#9ccb3b")
        self.kin_number = Label(master, text="Cell Phone Number: ")
        self.kin_number.place(x=150, y=450)
        self.kin_number.config(bg="white")
        self.kinnumber_entry = Entry(master)
        self.kinnumber_entry.place(x=135, y=500)
        self.kinnumber_entry.config(bg="#9ccb3b")
        self.visitbtn = Button(master, text="Begin the visit", command=self.visitor)
        self.visitbtn.place(x=150, y=550)
        self.visitbtn.config(bg="green", borderwidth="10")
        self.backbtn = Button(master, text="Back", command=self.Back)
        self.backbtn.place(x=10, y=570)
        self.backbtn.config(bg="green", borderwidth="5")
        self.logout = Button(master, text="Log out", command=self.LOGout)
        self.logout.place(x=355, y=570)
        self.logout.config(bg="green", borderwidth="5", state="disabled")
    def Back(self):
        root.destroy()
        import First
    def LOGout(self):
        root.destroy()
        import logoutvisitors
    #function for visitors sign in
    def visitor(self):
        try:
            if self.name_entry.get() == "":
                messagebox.showerror('STATUS', "Invalid, please fill in all the required information")
            elif self.ID_entry.get() == "":
                messagebox.showerror('STATUS', "Invalid, please fill in all the required information")
            elif self.no_entry.get() == "":
                messagebox.showerror('STATUS', "Invalid, please fill in all the required information")
            elif self.kinname_entry.get() == "":
                messagebox.showerror('STATUS', "Invalid, please fill in all the required information")
            elif self.kinnumber_entry.get() == "":
                messagebox.showerror('STATUS', "Invalid, please fill in all the required information")
            elif len(self.no_entry.get()) != 10:
                messagebox.showerror('STATUS', "Please enter a valid phone number")
            elif len(self.kinnumber_entry.get()) != 10:
                messagebox.showerror('STATUS', "Please enter a valid phone number")
            elif len(self.ID_entry.get()) != 13:
                messagebox.showerror('STATUS', "Invalid ID")
            else:
                now = datetime.datetime.now()
                signin_time = now.strftime("%y-%m-%d %H:%M:%S")
                db = mysql.connector.connect(
                        host='127.0.0.1',
                        user='lifechoices',
                        password='@Lifechoices1234',
                        auth_plugin='mysql_native_password',
                        database='sign_up_and_log_in'
                        )
                cursor = db.cursor()
                code = "INSERT INTO visitors (name, id_number, cell_number, next_of_kin_name, next_of_kin_number, sign_in) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (self.name_entry.get(), self.ID_entry.get(), self.no_entry.get(), self.kinname_entry.get(), self.kinnumber_entry.get(), signin_time)
                cursor.execute(code, values)
                db.commit()
                self.logout.config(state="normal")
                messagebox.showinfo('WELCOME', "you have offically began your visit to Lifechoices Academy, when you leave the premise please sign out by clicking the log out button and follow the steps")
        except ValueError:
            if self.name_entry.get() != str:
                messagebox.showerror('STATUS', "Invalid, please provide letters not numbers for the name")
            elif self.kinname_entry.get() != str:
                messagebox.showerror('STATUS', "Invalid, please provide letters not numbers for the name")

w = visit(root)
root.mainloop()
