from tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.instruction = Label(self, text = "Enter the password")
        self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        self.password = Entry(self)
        self.password.grid(row = 1, column = 1, sticky = W)

        self.submit_button = Button(self, text = "Submit", command = self.reveal)
        self.submit_button.grid(row = 2, column = 0, sticky = W)

        self.text = Text(self, width = 35, height = 5, wrap = WORD)
        self.text.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        content = self.password.get()
        if content == "password":
            message = "You have access to something special"
        else:
            message = "Access denied."
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)
        
root = Tk()
root.title("Password")
root.geometry("250x150")

app = Application(root)

root.mainloop()
