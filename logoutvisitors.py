#the visitors sign out window inserts the time the visitor leave the premise
from tkinter import *
import mysql.connector
from tkinter import messagebox
import datetime

hold = Tk()
hold.title("Log out")
hold.geometry("450x300")
hold.config(bg="green")
class LogOut:
    def __init__(self, master):
        self.name = Label(master, text="Enter your name and surname: ")
        self.name.place(x=130, y=20)
        self.name.config(bg="green")
        self.name_entry = Entry(master)
        self.name_entry.place(x=145, y=50)
        self.name_entry.config(bg="white")
        self.id_number = Label(master, text="Enter your ID number: ")
        self.id_number.place(x=155, y=100)
        self.id_number.config(bg="green")
        self.id_entry = Entry(master)
        self.id_entry.place(x=145, y=150)
        self.id_entry.config(bg="white")
        self.logbtn = Button(master, text="log out", command=self.logOut)
        self.logbtn.place(x=190, y=200)
        self.logbtn.config(bg="white", borderwidth="10")
    def logOut(self):
        try:
            if self.name_entry.get() == "":
                messagebox.showerror('ERROR', "Invalid entry")
            elif self.id_entry.get() == "":
                messagebox.showerror('ERROR', "Invalid entry")
            elif len(self.id_entry.get()) != 13:
                messagebox.showerror('ERROR', "Invalid ID number")
            else:
                now = datetime.datetime.now()
                signout_time = now.strftime("%y-%m-%d %H:%M:%S")
                db = mysql.connector.connect(
                    host='127.0.0.1',
                    user='lifechoices',
                    password='@Lifechoices1234',
                    auth_plugin='mysql_native_password',
                    database='sign_up_and_log_in'
                    )
                my_cursor = db.cursor()
                code = "UPDATE visitors SET sign_out=%s WHERE id_number=%s"
                values = (signout_time, self.id_entry.get())
                my_cursor.execute(code, values)
                db.commit()
                messagebox.showinfo('GOODBYE', "We hope you enjoyed your time see you next time.")
        except ValueError:
            if self.id_entry.get() != int:
                messagebox.showerror('ERROR', "Please enter a valid ID number")
y = LogOut(hold)
hold.mainloop()
