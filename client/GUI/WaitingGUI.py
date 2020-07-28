import tkinter as tk

def createWaitingMenu(root):
    #creates the frame for the waiting menu
    waitingFrame = tk.Frame(root, height=320, width=300)

    #sets the text label in the frame
    waitingLabel = tk.Label(waitingFrame, text="Waiting for players")
    waitingLabel.place(relx=0.5, rely=0.5, anchor="center")

    #returns the frame
    return waitingFrame