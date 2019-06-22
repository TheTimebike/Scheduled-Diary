from interface import Interface
from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    root.geometry("1100x530")
    interface = Interface(root)
    root.mainloop()