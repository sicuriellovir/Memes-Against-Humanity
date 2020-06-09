import tkinter as tk
import GUIhandler as GUI

def createReadyMenu(root):
    readyFrame = tk.Frame(root, height=300, width=300)

    readyButton = tk.Button(readyFrame, text="Click when ready")
    readyButton.place(height=40, width=100, relx=0.5, rely=0.5, anchor="center")

    returnButton = tk.Button(readyFrame, text="Return to menu")
    returnButton.place(height=40, width=100, relx=0.5, rely=0.5, y=100, anchor="center")

    # need to code to send information to server when player selects ready
    def readyEvent(event):
        readyButton.configure(state='disabled')
        returnButton.configure(state='disabled')
    readyButton.bind('<Button-1>', readyEvent)

    def returnEvent(event):
        readyFrame.forget()
        GUI.showMainMenu()
    returnButton.bind('<Button-1>', returnEvent)

    return readyFrame