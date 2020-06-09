import tkinter as tk
import GUIhandler as GUI

def createMainMenu(root):
    #creates the frame for the main menu
    mainFrame = tk.Frame(root, height=300, width=300)

    #adds buttons to the frame and sets their position
    startButton = tk.Button(mainFrame, text="Connect to game")
    optionsButton = tk.Button(mainFrame, text="Options")
    exitButton = tk.Button(mainFrame, text="Exit")
    startButton.place(height=40, width=100, relx=0.5, rely=0.5, y=-100, anchor="center")
    optionsButton.place(height=40, width=100, relx=0.5, rely=0.5, anchor="center")
    exitButton.place(height=40, width=100, relx=0.5, rely=0.5, y=100, anchor="center")

    #runs if the user clicks "Connect to game"
    def connectGameEvent(event):
        mainFrame.forget()
        GUI.showReadyMenu()
    startButton.bind('<Button-1>', connectGameEvent)

    #runs if the user clicks "Options"
    def optionsMenuEvent(event):
        GUI.showOptionsWindow()
    optionsButton.bind('<Button-1>', optionsMenuEvent)

    #runs if the user clicks "Exit"
    def quitEvent(event):
        GUI.exit()
    exitButton.bind('<Button-1>', quitEvent)

    #returns the frame we created
    return mainFrame