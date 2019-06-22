from tkinter import *
from scheduler import Scheduler
from saver import Saver

class Prompt():
    def __init__(self):
        pass

class Interface(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Diary Prompter")
        self.init_elements()
        self.saver = Saver()

    def init_elements(self):
        self.label_1 = Label(
            self.master,
            text="I want a prompt every"
        )
        self.label_1.place(x=10, y=10)

        self.text_box = Entry(
            self.master,
            width=20
        )
        self.text_box.place(x=10, y=30)

        self.option_menu_default = StringVar()
        self.option_menu_default.set("hours")
        self.option_menu = OptionMenu(
            self.master,
            self.option_menu_default,
            "seconds", 
            "minutes", 
            "hours", 
            "days",
        )
        self.option_menu.place(x=8, y=55)

        self.start_button = Button(
            self.master,
            width=20, height=5,
            text="Start!", 
            command=lambda: self.start_button_command()
        )
        self.start_button.place(x=140, y=10)

    def start_button_command(self):
        self.scheduler = Scheduler(self)

    def trigger_prompt(self):
        self.saver._new_entry()
        print("lol")

if __name__ == "__main__":
    root = Tk()
    root.geometry("300x120")
    interface = Interface(root)
    root.mainloop()