from tkinter import *
from scheduler import Scheduler
from saver import Saver

class Prompt():
    def __init__(self, main_window):
        self.main_window = main_window
        self.sub_window = Toplevel(self.main_window.master)
        self.sub_window.wm_title("Diary Entry Time!")
        self.sub_window.resizable(False, False)

        self.text_box = Text(
            self.sub_window,
            width=84,
            height=10
        )
        self.text_box.place(x=10, y=10)

        self.submit_button = Button(
            self.sub_window,
            width=96,
            height=3,
            text="Submit!",
            command=lambda: self.submit_entry()
        )
        self.submit_button.place(x=10, y=180)

        self.sub_window.geometry("700x250")

    def submit_entry(self):
        entry = self.text_box.get('1.0', END)
        self.main_window.saver._new_entry(entry)
        self.sub_window.destroy()

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
        timer = self.text_box.get()
        timer_measurement = self.option_menu_default.get()
        self.scheduler = Scheduler(self, timer=timer, timer_measurement=timer_measurement)

    def trigger_prompt(self):
        Prompt(self)

if __name__ == "__main__":
    root = Tk()
    root.geometry("300x120")
    interface = Interface(root)
    root.resizable(False, False)
    root.mainloop()