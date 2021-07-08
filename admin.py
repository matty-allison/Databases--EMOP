# the Admin window only avalible from the first window but pressing Control a
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

root = Tk()
root.title('Admin')
root.geometry('870x500')
root.config(bg="green")
class Admin:
    #this function is used to display the info that has been inserted into the database onto the treeview
    def __init__(self, master):
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
        total = cursor.rowcount
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
        for y in list:
            value = y
            self.tree.insert('', 'end', values=value)
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
        self.update = Button(master, text="Update", command=self.Update)
        self.update.place(x=300, y=400)
        self.update.config(bg="#9ccb3b", borderwidth="5")
        self.delete = Button(master, text="Delete", command=self.Delete)
        self.delete.place(x=450, y=400)
        self.delete.config(bg="#9ccb3b", borderwidth="5")
        self.exit = Button(master, text="Exit", command=self.Exit)
        self.exit.place(x=600, y=400)
        self.exit.config(bg="#9ccb3b", borderwidth="5")
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
                code = "DELETE FROM mytable_students WHERE id_number='%s'"
                values = (self.id_entry.get())
                cursor.execute(code, values)
                db.commit()
                messagebox.showinfo('CHANGE', "Record deleted")
        except ValueError:
            if self.id_entry.get() != int:
                messagebox.showerror('ERROR', "Enter a valid id number")
    #an exit function
    def Exit(self):
        root.destroy()
        import First

x=Admin(root)
root.mainloop()
