import tkinter as tk
from tkinter.ttk import *

def createMainMenu():
    window = tk.Tk()
    window.geometry("700x500")

    startButton = tk.Button(text="Start")
    optionsButton = tk.Button(text="Options")
    exitButton = tk.Button(text="Exit")
    startButton.place(relheight=0.1, relwidth=0.2, relx=0.5, rely=0.5, y=-100, anchor = "center")
    optionsButton.place(relheight=0.1, relwidth=0.2, relx=0.5, rely=0.5, anchor="center")
    exitButton.place(relheight=0.1, relwidth=0.2, relx=0.5, rely=0.5, y=100, anchor="center")
    
    window.mainloop()

__package__ = "GUI"