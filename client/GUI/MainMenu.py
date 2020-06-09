import tkinter as tk
from tkinter.ttk import *

def createMainMenu():
    window = tk.Tk()
    window.geometry("700x500")
    testLabel = tk.Label(text="test")
    testLabel.pack()
    window.mainloop()

__package__ = "GUI"