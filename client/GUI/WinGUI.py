import tkinter as tk
from . import GUIhandler as GUI

def createWinGUI(root):
    winFrame = tk.Frame(root, height=320, width=300)
    winLabel = tk.Label(winFrame, text="You won!", wraplength=300, justify="center")
    winLabel.place(height=50, width=150, relx=0.5, y=0,  rely=0.5, anchor="center")
    exitButton = tk.Button(winFrame, text="Exit")
    exitButton.place(height=50, width=50, relx=0.5, y=100,  rely=0.5, anchor="center")

    def exitEvent(event):
        GUI.exit()
    exitButton.bind('<Button-1>', exitEvent)

    return winFrame