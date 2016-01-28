from tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.button1 = Button(self, text = "This is the first button")
        self.button1.grid()

        self.button2 = Button(self)
        self.button2.grid()
        self.button2.configure(text = "This is the second")
        
        self.button3 = Button(self)
        self.button3.grid()
        self.button3["text"] = "This is the third"
root = Tk()
root.title("Lazy Buttons")
root.geometry("200x85")

app = Application(root)

root.mainloop()
