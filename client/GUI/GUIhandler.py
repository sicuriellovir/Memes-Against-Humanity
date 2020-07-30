import tkinter as tk
from .. import client
from ..Player import Player
from ..Card import PhraseCard, MemeCard
from . import MainMenu as menu
from . import ReadyGUI as ready
from . import OptionsGUI as options
from . import PlayerGUI as pGUI
from . import JudgingGUI as jGUI
from . import WinGUI as win
from . import LossGUI as loss

#creates the main window with size 300x300 and makes it non-resizable
root = tk.Tk()
root.geometry("320x300")
root.resizable(False, False)
root.title("Memes Against Humanity")

#gets the frames that can be stored in the window (just main menu and ready menu at this point)
menuFrame = menu.createMainMenu(root)
readyFrame = ready.createReadyMenu(root)
winFrame = win.createWinGUI(root)
lossFrame = loss.createLossGUI(root)

player = 0

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

#sets the player frame in the window. Takes in a list of 3 PhraseCards and a MemeCard
def showPlayerGUI(playerName):
    global player
    if player == 0:
        player = Player(playerName)
    meme = MemeCard(client.getCurrentMeme())
    playerFrame = pGUI.createPlayerMenu(root, player, meme)
    global currentFrame
    currentFrame.forget()
    currentFrame = playerFrame
    root.geometry("600x500")
    packCurrentFrame()

#sets the judging frame in the window
def showJudgingGUI(player):
    phrases = client.getJudgingPhraseCards()
    phrases[0] = PhraseCard(phrases[1], phrases[0])
    phrases[1] = PhraseCard(phrases[3], phrases[2])
    meme = MemeCard(client.getCurrentMeme())
    judgingFrame = jGUI.createJudgingMenu(root, phrases, meme, player)
    global currentFrame
    currentFrame.forget()
    currentFrame = judgingFrame
    root.geometry("600x500")
    packCurrentFrame()

def showWinGUI():
    global currentFrame
    currentFrame.forget()
    currentFrame = winFrame
    root.geometry("320x300")
    packCurrentFrame()

def showLossGUI():
    global currentFrame
    currentFrame.forget()
    currentFrame = lossFrame
    root.geometry("320x300")
    packCurrentFrame()

#packs currentFrame into the window
def packCurrentFrame():
    currentFrame.pack()
    root.mainloop()

#runs when the program exist. Doesn't end the program, just deletes the window and its frames
def exit():
    root.destroy()