# the Admin window only avalible from the first window but pressing Control a
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

root = Tk()
root.title('Admin')
root.geometry('870x600')
root.config(bg="green")
class Admin:
    #this function is used to display the info that has been inserted into the database onto the treeview
    def __init__(self, master):
        #this is the treeview design
        self.tree = ttk.Treeview(master)
        self.tree['columns'] = ('Name', 'ID number', 'Cell number', 'Next of kin(name)', 'Next of kin(Number)', 'Sign in', 'Sign out')
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('Name', anchor=CENTER, width=120)
        self.tree.column('ID number', anchor=CENTER, width=120)
        self.tree.column('Cell number', anchor=CENTER, width=100)
        self.tree.column('Next of kin(name)', anchor=CENTER, width=120)
        self.tree.column('Next of kin(Number)', anchor=CENTER, width=100)
        self.tree.column('Sign in', anchor=CENTER, width=150)
        self.tree.column('Sign out', anchor=CENTER, width=150)

        self.tree.heading('#0', text='', anchor=CENTER)
        self.tree.heading('Name', text='Name', anchor=CENTER)
        self.tree.heading('ID number', text='Id number', anchor=CENTER)
        self.tree.heading('Cell number', text='Cell number', anchor=CENTER)
        self.tree.heading('Next of kin(name)', text='kin name', anchor=CENTER)
        self.tree.heading('Next of kin(Number)', text='kin Number', anchor=CENTER)
        self.tree.heading('Sign in', text='Sign in', anchor=CENTER)
        self.tree.heading('Sign out', text='Sign out', anchor=CENTER)
        #this is where the insert of the information happens in order to see the peoples details
        self.tree.pack()
        self.name = Entry(master)
        self.name.place(x=30, y=300)
        self.namelabel = Label(master, text="Enter name: ")
        self.namelabel.place(x=40, y=250)
        self.namelabel.config(bg="green")
        self.id_entry = Entry(master)
        self.id_entry.place(x=230, y=300)
        self.id_label = Label(master, text="Enter Id number: ")
        self.id_label.place(x=240, y=250)
        self.id_label.config(bg="green")
        self.number = Entry(master)
        self.number.place(x=430, y=300)
        self.number_label = Label(master, text="Enter cell number: ")
        self.number_label.place(x=440, y=250)
        self.number_label.config(bg="green")
        self.kin_name = Entry(master)
        self.kin_name.place(x=630, y=300)
        self.kin_name_label = Label(master, text="Enter next of kin name: ")
        self.kin_name_label.place(x=630, y=250)
        self.kin_name_label.config(bg="green")
        self.kin_number = Entry(master)
        self.kin_number.place(x=30, y=400)
        self.kin_number_label = Label(master, text="Enter next of kin number: ")
        self.kin_number_label.place(x=30, y=350)
        self.kin_number_label.config(bg="green")
        self.students = Button(master, text="Students", command=self.studentrecords)
        self.students.place(x=250, y=390)
        self.students.config(bg="green", borderwidth="5")
        self.visitors = Button(master, text="Visitors", command=self.visitorrecords)
        self.visitors.place(x=400, y=390)
        self.visitors.config(bg="green", borderwidth="5")
        self.insert = Button(master, text="Insert in to students", command=self.insertrecord)
        self.insert.place(x=30, y=500)
        self.insert.config(bg="#9ccb3b", borderwidth="5")
        self.insertv = Button(master, text="Insert in to visitors", command=self.insertrecordv)
        self.insertv.place(x=220, y=500)
        self.insertv.config(bg="#9ccb3b", borderwidth="5")
        self.update = Button(master, text="Update", command=self.Update)
        self.update.place(x=450, y=500)
        self.update.config(bg="#9ccb3b", borderwidth="5")
        self.delete = Button(master, text="Delete", command=self.Delete)
        self.delete.place(x=580, y=500)
        self.delete.config(bg="#9ccb3b", borderwidth="5")
        self.exit = Button(master, text="Exit", command=self.Exit)
        self.exit.place(x=700, y=500)
        self.exit.config(bg="#9ccb3b", borderwidth="5")
    # Function to display student records
    def studentrecords(self):
        db = mysql.connector.connect(
                        host='127.0.0.1',
                        user='lifechoices',
                        password='@Lifechoices1234',
                        auth_plugin='mysql_native_password',
                        database='sign_up_and_log_in'
                        )
        cursor = db.cursor()
        code = "select * from sign_up_and_log_in.mytable_students "
        cursor.execute(code)
        list = cursor.fetchall()
        for y in list:
            value = y
            self.tree.insert('', 'end', values=value)
    # Function to display visitor records
    def visitorrecords(self):
        db = mysql.connector.connect(
                        host='127.0.0.1',
                        user='lifechoices',
                        password='@Lifechoices1234',
                        auth_plugin='mysql_native_password',
                        database='sign_up_and_log_in'
                        )
        cursor = db.cursor()
        code = "select * from sign_up_and_log_in.visitors"
        cursor.execute(code)
        list = cursor.fetchall()
        for y in list:
            value = y
            self.tree.insert('', 'end', values=value)

    #function for updating uses info
    def Update(self):
        try:
            if self.name.get() == "":
                messagebox.showerror('ERROR', "Enter a name please")
            elif self.id_entry.get() == "":
                messagebox.showerror('ERROR', "Enter a ID number")
            elif self.number.get() == "":
                messagebox.showerror('ERROR', "Enter a number")
            elif len(self.id_entry.get()) != 13:
                messagebox.showerror('ERROR', "Enter a Valid ID number")
            elif len(self.number.get()) != 10:
                messagebox.showerror('ERROR', "Enter a valid phone number")
            elif len(self.kin_number.get()) != 10:
                messagebox.showerror('ERROR', "Enter a valid phone number")
            else:
                db = mysql.connector.connect(
                        host='127.0.0.1',
                        user='lifechoices',
                        password='@Lifechoices1234',
                        auth_plugin='mysql_native_password',
                        database='sign_up_and_log_in'
                        )
                cursor = db.cursor()
                code = ""
                values = ()
                cursor.execute(code, values)
                db.commit()
                messagebox.showinfo('CHANGED', "Record changed")

        except ValueError:
            if self.id_entry.get() != int:
                messagebox.showerror('ERROR', "Enter a valid id number")
    #function for Deleting of old users or a user whos info is no longer needed
    def Delete(self):
        try:
            if self.name.get() == "":
                messagebox.showerror('ERROR', "Enter a name please")
            elif self.id_entry.get() == "":
                messagebox.showerror('ERROR', "Enter a ID number")
            elif self.number.get() == "":
                messagebox.showerror('ERROR', "Enter a number")
            elif len(self.id_entry.get()) != 13:
                messagebox.showerror('ERROR', "Enter a Valid ID number")
            elif len(self.number.get()) != 10:
                messagebox.showerror('ERROR', "Enter a valid phone number")
            elif len(self.kin_number.get()) != 10:
                messagebox.showerror('ERROR', "Enter a valid phone number")
            else:
                db = mysql.connector.connect(
                        host='127.0.0.1',
                        user='lifechoices',
                        password='@Lifechoices1234',
                        auth_plugin='mysql_native_password',
                        database='sign_up_and_log_in'
                        )
                cursor = db.cursor()
                code = ""
                values = (self.id_entry.get())
                cursor.execute(code, values)
                db.commit()
                messagebox.showinfo('CHANGE', "Record deleted")
        except ValueError:
            if self.id_entry.get() != int:
                messagebox.showerror('ERROR', "Enter a valid id number")
    # Function to insert records into students
    def insertrecord(self):
        try:
            if self.name.get() == "":
                messagebox.showerror('ERROR', "Invalid, please fill in all the required information")
            elif self.id_entry.get() == "":
                messagebox.showerror('ERROR', "Invalid, please fill in all the required information")
            elif self.number.get() == "":
                messagebox.showerror('ERROR', "Invalid, please fill in all the required information")
            elif self.kin_name.get() == "":
                messagebox.showerror('ERROR', "Invalid, please fill in all the required information")
            elif self.kin_number.get() == "":
                messagebox.showerror('ERROR', "Invalid, please fill in all the required information")
            elif len(self.number.get()) != 10:
                messagebox.showerror('ERROR', "Please enter a valid phone number")
            elif len(self.kin_number.get()) != 10:
                messagebox.showerror('ERROR', "Please enter a valid phone number")
            elif len(self.id_entry.get()) != 13:
                messagebox.showerror('ERROR', "Invalid ID")
            else:
                db = mysql.connector.connect(
                        host='127.0.0.1',
                        user='lifechoices',
                        password='@Lifechoices1234',
                        auth_plugin='mysql_native_password',
                        database='sign_up_and_log_in'
                        )
                cursor = db.cursor()
                code = "INSERT INTO mytable_students (name, id_number, cell_number, next_of_kin_name, next_of_kin_number) VALUES (%s, %s, %s, %s, %s)"
                values = (self.name.get(), self.id_entry.get(), self.number.get(), self.kin_name.get(), self.kin_number.get())
                cursor.execute(code, values)
                db.commit()
                messagebox.showinfo('Changed', "Record inserted")
        except ValueError:
            if self.name.get() != str:
                messagebox.showerror('ERROR', "Invalid, please provide letters not numbers for the name")
            elif self.kin_number.get() != str:
                messagebox.showerror('ERROR', "Invalid, please provide letters not numbers for the name")
    # Function to insert records into students
    def insertrecordv(self):
        try:
            if self.name.get() == "":
                messagebox.showerror('ERROR', "Invalid, please fill in all the required information")
            elif self.id_entry.get() == "":
                messagebox.showerror('ERROR', "Invalid, please fill in all the required information")
            elif self.number.get() == "":
                messagebox.showerror('ERROR', "Invalid, please fill in all the required information")
            elif self.kin_name.get() == "":
                messagebox.showerror('ERROR', "Invalid, please fill in all the required information")
            elif self.kin_number.get() == "":
                messagebox.showerror('ERROR', "Invalid, please fill in all the required information")
            elif len(self.number.get()) != 10:
                messagebox.showerror('ERROR', "Please enter a valid phone number")
            elif len(self.kin_number.get()) != 10:
                messagebox.showerror('ERROR', "Please enter a valid phone number")
            elif len(self.id_entry.get()) != 13:
                messagebox.showerror('ERROR', "Invalid ID")
            else:
                db = mysql.connector.connect(
                        host='127.0.0.1',
                        user='lifechoices',
                        password='@Lifechoices1234',
                        auth_plugin='mysql_native_password',
                        database='sign_up_and_log_in'
                        )
                cursor = db.cursor()
                code = "INSERT INTO visitors (name, id_number, cell_number, next_of_kin_name, next_of_kin_number) VALUES (%s, %s, %s, %s, %s)"
                values = (self.name.get(), self.id_entry.get(), self.number.get(), self.kin_name.get(), self.kin_number.get())
                cursor.execute(code, values)
                db.commit()
                messagebox.showinfo('Changed', "Record inserted")
        except ValueError:
            if self.name.get() != str:
                messagebox.showerror('ERROR', "Invalid, please provide letters not numbers for the name")
            elif self.kin_number.get() != str:
                messagebox.showerror('ERROR', "Invalid, please provide letters not numbers for the name")
    #an exit function
    def Exit(self):
        root.destroy()
        import First

x=Admin(root)
root.mainloop()
