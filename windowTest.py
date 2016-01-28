from tkinter import *

root = Tk()

root.title("Labeler")
root.geometry("400x200")

app = Frame(root)
app.grid()

buttons = ["Carter", "Mom", "Dad", "Chase", "Gus", "Emmett"]

for btn in buttons:
    btn = Button(app, text=btn + "'s Button")
    btn.grid()

root.mainloop()
