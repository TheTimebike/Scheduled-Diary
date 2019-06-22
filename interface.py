from tkinter import *
from scheduler import Scheduler

class Interface(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Diary Prompter")
        self.scheduler = Scheduler(self)

    def trigger_prompt(self):
        print("lol")