import tkinter as tk
import GUIhandler as GUI

def createReadyMenu(root):
    #creates the frame for the ready menu
    readyFrame = tk.Frame(root, height=300, width=300)

    #adds buttons to the frame and sets their position
    readyButton = tk.Button(readyFrame, text="Click when ready")
    returnButton = tk.Button(readyFrame, text="Return to menu")
    readyButton.place(height=40, width=100, relx=0.5, rely=0.5, anchor="center")
    returnButton.place(height=40, width=100, relx=0.5, rely=0.5, y=100, anchor="center")

    #need to code to send information to server when player selects ready
    #at this point it disables the ready and return buttons when the user clicks the ready button
    def readyEvent(event):
        readyButton.configure(state='disabled')
        returnButton.configure(state='disabled')
    readyButton.bind('<Button-1>', readyEvent)

    #returns to the main menu if the user clicks the return button
    def returnEvent(event):
        readyFrame.forget()
        GUI.showMainMenu()
    returnButton.bind('<Button-1>', returnEvent)

    #returns the frame we created
    return readyFrame