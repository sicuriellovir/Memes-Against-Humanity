import tkinter as tk
import GUIhandler as GUI

def createMainMenu(root):
    mainFrame = tk.Frame(root, height=300, width=300)

    startButton = tk.Button(mainFrame, text="Connect to game")
    optionsButton = tk.Button(mainFrame, text="Options")
    exitButton = tk.Button(mainFrame, text="Exit")
    startButton.place(height=40, width=100, relx=0.5, rely=0.5, y=-100, anchor="center")
    optionsButton.place(height=40, width=100, relx=0.5, rely=0.5, anchor="center")
    exitButton.place(height=40, width=100, relx=0.5, rely=0.5, y=100, anchor="center")

    def connectGameEvent(event):
        mainFrame.forget()
        GUI.showReadyMenu()
    startButton.bind('<Button-1>', connectGameEvent)

    def optionsMenuEvent(event):
        GUI.showOptionsWindow()
    optionsButton.bind('<Button-1>', optionsMenuEvent)

    def quitEvent(event):
        GUI.exit()
    exitButton.bind('<Button-1>', quitEvent)

    return mainFrame