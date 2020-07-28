import tkinter as tk
from . import MainMenu as menu
from . import ReadyGUI as ready
from . import OptionsGUI as options
from . import WaitingGUI as waiting
from . import PlayerGUI as pGUI
from . import JudgingGUI as jGUI

#creates the main window with size 300x300 and makes it non-resizable
root = tk.Tk()
root.geometry("320x300")
root.resizable(False, False)
root.title("Memes Against Humanity")

#gets the frames that can be stored in the window (just main menu and ready menu at this point)
menuFrame = menu.createMainMenu(root)
readyFrame = ready.createReadyMenu(root)
waitingFrame = waiting.createWaitingMenu(root)

currentFrame = menuFrame
#sets the menu frame in the window
def showMainMenu():
    global currentFrame
    currentFrame.forget()
    currentFrame = menuFrame
    root.geometry("320x300")
    packCurrentFrame()

#sets the ready frame in the window
def showReadyMenu():
    global currentFrame
    currentFrame.forget()
    currentFrame = readyFrame
    root.geometry("320x300")
    packCurrentFrame()

#creates a seperate window for the options
def showOptionsWindow():
    options.createOptionsWindow()

#sets the waiting frame in the window. checks if the server
#is ready for us to proceed to the next window every .1 seconds
def showWaitingGUI():
    global currentFrame
    currentFrame.forget()
    currentFrame = waitingFrame
    root.geometry("320x300")
    #root.after(100, checkIfReady)
    packCurrentFrame()

#sets the player frame in the window. Takes in a list of 3 PhraseCards and a MemeCard
def showPlayerGUI(pCards, mCard):
    playerFrame = pGUI.createPlayerMenu(root, pCards, mCard)
    global currentFrame
    currentFrame.forget()
    currentFrame = playerFrame
    root.geometry("600x500")
    packCurrentFrame()

#sets the judging frame in the window. Takes in a Player object, a list of 3
#PhraseCards (1 from each player), and a MemeCard
def showJudgingGUI(player, pCards, mCard):
    #judgingFrame = jGUI.createJudgingMenu(root, pCards, mCard, player.isJudge())
    judgingFrame = jGUI.createJudgingMenu(root, pCards, mCard, True)
    global currentFrame
    currentFrame.forget()
    currentFrame = judgingFrame
    root.geometry("600x500")
    packCurrentFrame()

#packs currentFrame into the window
def packCurrentFrame():
    currentFrame.pack()
    root.mainloop()

#def checkIfReady():
#    if client.isReady():
#        showJudgingGUI(client.getPlayer(), client.getJudgingPhraseCards(), client.getJudgingMemeCard)

#runs when the program exist. Doesn't end the program, just deletes the window and its frames
def exit():
    menuFrame.destroy()
    readyFrame.destroy()
    waitingFrame.destroy()
    root.destroy()