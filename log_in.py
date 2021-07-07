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
        self.logbtn = Button(master, text="log in", command=self.logIn)
        self.logbtn.place(x=190, y=200)
        self.logbtn.config(bg="#9ccb3b", borderwidth="10")
        self.backbtn = Button(master, text="Back", command=self.Back)
        self.backbtn.place(x=10, y=250)
        self.backbtn.config(bg="#9ccb3b", borderwidth="5")
        self.logout = Button(master, text="Log out", command=self.LOGout)
        self.logout.place(x=350, y=250)
        self.logout.config(bg="green", borderwidth="5", state="disabled")

    def Back(self):
        box.destroy()
        import First
    def LOGout(self):
        box.destroy()
        import logoutstudents

    def logIn(self):
        try:
            if self.name_entry.get() == "":
                messagebox.showerror('ERROR', "Invalid, Please enter the required information.")
            elif self.id_entry.get() == "":
                messagebox.showerror('ERROR', "Invalid, Please enter the required information.")
            elif len(self.id_entry.get()) != 13:
                messagebox.showerror('ERROR', "Invalid, Please enter a valid ID number.")
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
                my_cursor = db.cursor()
                code = "UPDATE mytable_students SET sign_in=%s WHERE id_number=%s"
                values = (signin_time, self.id_entry.get())
                my_cursor.execute(code, values)
                db.commit()
                self.logout.config(state="normal")
                messagebox.showinfo('WELCOME', "Welcome back student")
        except ValueError:
            if self.id_entry.get() != int:
                messagebox.showerror('ERROR', "Invalid ID")

x = log(box)
box.mainloop()
