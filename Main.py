from interface import Interface
from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    root.geometry("300x120")
    interface = Interface(root)
    root.resizable(False, False)
    root.mainloop()