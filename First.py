from tkinter import *

root = Tk()
root.title("Welcome to Lifechoices Academy")
root.config(bg="Green")
root.geometry("450x355")

class Weclome:
    canvas = Canvas(root, width=300, height=80)
    canvas.place(x=75, y=10)
    img = PhotoImage(file="Logo-Life-Choices-300x80.png")
    canvas.create_image(150, 40, image=img)
    def __init__(self, master):
        self.label = Label(master, text="Click the appropriate button: ")
        self.label.place(x=95, y=100)
        self.label.config(bg="green", font=("bold", 13))
        self.sign = Button(master, text="Sign up", command=self.Signup)
        self.sign.place(x=175, y=150)
        self.sign.config(bg="#9ccb3b", borderwidth="10")
        self.log = Button(master, text="Log in", command=self.Login)
        self.log.place(x=180, y=220)
        self.log.config(bg="#9ccb3b", borderwidth="10")
        self.visiting = Button(master, text="Just Visiting", command=self.Visit)
        self.visiting.place(x=162, y=290)
        self.visiting.config(bg="#9ccb3b", borderwidth="10")

    def Signup(self):
        root.destroy()
        import sign_up

    def Login(self):
        root.destroy()
        import log_in

    def Visit(self):
        root.destroy()
        import visitors

y = Weclome(root)
root.mainloop()
