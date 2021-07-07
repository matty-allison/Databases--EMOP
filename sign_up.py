from tkinter import *
import mysql.connector
from tkinter import messagebox
import datetime

window = Tk()
window.title("Sign up to lifechoices today!")
window.config(bg="green")
window.geometry("450x620")

class sign:
    def __init__(self, master):
        self.name = Label(master, text="Please enter your name and surname: ")
        self.name.place(x=100, y=10)
        self.name.config(bg="green")
        self.name_entry = Entry(master)
        self.name_entry.place(x=135, y=50)
        self.name_entry.config(bg="#9ccb3b")
        self.ID = Label(master, text="Please enter your ID number: ")
        self.ID.place(x=120, y=100)
        self.ID.config(bg="green")
        self.ID_entry = Entry(master)
        self.ID_entry.place(x=135, y=150)
        self.ID_entry.config(bg="#9ccb3b")
        self.number = Label(master, text="Please enter your cell phone number: ")
        self.number.place(x=100, y=200)
        self.number.config(bg="green")
        self.no_entry = Entry(master)
        self.no_entry.place(x=135, y=250)
        self.no_entry.config(bg="#9ccb3b")
        self.kin = Label(master, text="Please enter your next of kin's information: ")
        self.kin.place(x=80, y=300)
        self.kin.config(bg="green", borderwidth="5")
        self.kin_name = Label(master, text="Name and Surname: ")
        self.kin_name.place(x=150, y=350)
        self.kin_name.config(bg="green")
        self.kinname_entry = Entry(master)
        self.kinname_entry.place(x=135, y=400)
        self.kinname_entry.config(bg="#9ccb3b")
        self.kin_number = Label(master, text="Cell Phone Number: ")
        self.kin_number.place(x=150, y=450)
        self.kin_number.config(bg="green")
        self.kinnumber_entry = Entry(master)
        self.kinnumber_entry.place(x=135, y=500)
        self.kinnumber_entry.config(bg="#9ccb3b")
        self.signbutton = Button(master, text="Sign up", command=self.signUP)
        self.signbutton.place(x=170, y=550)
        self.signbutton.config(bg="green", borderwidth="10")
        self.backbtn = Button(master, text="Back", command=self.Back)
        self.backbtn.place(x=10, y=570)
        self.backbtn.config(bg="green", borderwidth="5")
        self.logout = Button(master, text="Log out", command=self.LOGout)
        self.logout.place(x=355, y=570)
        self.logout.config(bg="green", borderwidth="5", state="disabled")
    def Back(self):
        window.destroy()
        import First
    def LOGout(self):
        window.destroy()
        import logoutstudents
    def signUP(self):
        try:
            if self.name_entry.get() == "":
                messagebox.showerror('ERROR', "Invalid, please fill in all the required information")
            elif self.ID_entry.get() == "":
                messagebox.showerror('ERROR', "Invalid, please fill in all the required information")
            elif self.no_entry.get() == "":
                messagebox.showerror('ERROR', "Invalid, please fill in all the required information")
            elif self.kinname_entry.get() == "":
                messagebox.showerror('ERROR', "Invalid, please fill in all the required information")
            elif self.kinnumber_entry.get() == "":
                messagebox.showerror('ERROR', "Invalid, please fill in all the required information")
            elif len(self.no_entry.get()) != 10:
                messagebox.showerror('ERROR', "Please enter a valid phone number")
            elif len(self.kinnumber_entry.get()) != 10:
                messagebox.showerror('ERROR', "Please enter a valid phone number")
            elif len(self.ID_entry.get()) != 13:
                messagebox.showerror('ERROR', "Invalid ID")
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
                code = "INSERT INTO mytable_students (name, id_number, cell_number, next_of_kin_name, next_of_kin_number, sign_in) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (self.name_entry.get(), self.ID_entry.get(), self.no_entry.get(), self.kinname_entry.get(), self.kinnumber_entry.get(), signin_time)
                cursor.execute(code, values)
                db.commit()
                self.logout.config(state="normal")
                messagebox.showinfo('WELCOME', "you have successfully signed up to Lifechoices Academy, when you leave the premise please sign out by clicking the log out button and follow the steps")
        except ValueError:
            if self.name_entry.get() != str:
                messagebox.showerror('ERROR', "Invalid, please provide letters not numbers for the name")
            elif self.kinname_entry.get() != str:
                messagebox.showerror('ERROR', "Invalid, please provide letters not numbers for the name")


x = sign(window)
window.mainloop()
