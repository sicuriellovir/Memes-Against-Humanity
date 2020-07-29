import tkinter as tk
from . import GUIhandler as GUI
from ..Card import PhraseCard, MemeCard
from time import sleep
from client.client import *

def createReadyMenu(root):
    #creates the frame for the ready menu
    readyFrame = tk.Frame(root, height=300, width=300)

    #adds buttons to the frame and sets their position
    readyButton = tk.Button(readyFrame, text="Click when ready")
    returnButton = tk.Button(readyFrame, text="Return to menu")
    nameLabel = tk.Label(readyFrame, text="Enter your username")
    nameTextBox = tk.Entry(readyFrame)
    nameLabel.place(relx=0.5, rely=0.5, y=-100, anchor="center")
    nameTextBox.place(relx=0.5, rely=0.5, y=-80, anchor="center")
    readyButton.place(height=40, width=100, relx=0.5, rely=0.5, anchor="center")
    returnButton.place(height=40, width=100, relx=0.5, rely=0.5, y=100, anchor="center")

    #need to code to send information to server when player selects ready
    def readyEvent(event):
        readyButton.configure(text="Waiting for players", state="disabled")
        returnButton.configure(state="disabled")
        root.update()
        client.Connect(nameTextBox.get())
        #GUI.showWaitingGUI()
        c1 = PhraseCard("TestPhrase5", "Player1")
        c2 = PhraseCard("TestPhrase2", "Player2")
        c3 = PhraseCard("TestPhrase26", "Player3")
        m1 = MemeCard("test.png")
        sleep(5)
        GUI.showPlayerGUI([c1, c2, c3], m1)
    readyButton.bind('<Button-1>', readyEvent)

    #returns to the main menu if the user clicks the return button
    def returnEvent(event):
        GUI.showMainMenu()
    returnButton.bind('<Button-1>', returnEvent)

    #returns the frame we created
    return readyFrame
