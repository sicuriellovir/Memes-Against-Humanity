import tkinter as tk
from . import GUIhandler as GUI

def createLossGUI(root):
    lossFrame = tk.Frame(root, height=320, width=300)
    lossLabel = tk.Label(lossFrame, text="You lost.", wraplength=300, justify="center")
    lossLabel.place(height=50, width=150, relx=0.5, y=0,  rely=0.5, anchor="center")
    exitButton = tk.Button(lossFrame, text="Exit")
    exitButton.place(height=50, width=50, relx=0.5, y=100,  rely=0.5, anchor="center")

    def exitEvent(event):
        GUI.exit()
    exitButton.bind('<Button-1>', exitEvent)

    return lossFrame