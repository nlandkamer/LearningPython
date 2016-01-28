from tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.button_clicks = 0 #counts num button clicks
        self.doom = 10
        self.create_widgets()
        
    def create_widgets(self):
        self.button = Button(self)
        self.button["text"] = "Total Clicks: 0"
        self.button["command"] = self.update_count
        self.button.grid()

        self.button2 = Button(self)
        self.button2["text"] = str(self.doom) + " Clicks Left till Doom!!!"
        self.button2["command"] = self.update_doom
        self.button2.grid()
        
    def update_count(self):
        self.button_clicks += 1
        self.button["text"] = "Total Clicks: " + str(self.button_clicks)

    def update_doom(self):
        if (self.doom > 0):
            self.doom -= 1
            if (self.doom > 0):
                self.button2["text"] = str(self.doom) + " Clicks Left till Doom!!!"
            else:
                self.button2["text"] = "DOOOOOOOOM!!!!!!"
        
root = Tk()
root.title("Lazy Buttons")
root.geometry("200x85")

app = Application(root)

root.mainloop()
