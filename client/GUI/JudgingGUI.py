import tkinter as tk
from .. import client
from . import GUIhandler as GUI
from PIL import ImageTk
from time import sleep

#creates the in-game judging GUI. Takes in a list of 2 PhraseCards (1 from each non-judge player) and a MemeCard
def createJudgingMenu(root, pCards, mCard, player):
    MEMECARDSIZE = (200, 200)

    #creates the frame for the in-game judging GUI
    playerFrame = tk.Frame(root, height=500, width=600)

    #sets the spaces for the players' chosen cards
    card1Label = tk.Label(playerFrame, text=pCards[0].getText(), wraplength=150, justify="center", borderwidth=2, relief="groove")
    card1Label.place(height=50, width=150, x=-200, relx=0.5, y=200, rely=0.5, anchor="center")
    card2Label = tk.Label(playerFrame, text=pCards[1].getText(), wraplength=150, justify="center", borderwidth=2, relief="groove")
    card2Label.place(height=50, width=150, relx=0.5, y=200,  rely=0.5, anchor="center")
    judgeLabel = tk.Label(playerFrame, text="You are the judge. Select a card.", wraplength=300, justify="center", borderwidth=2)
    notJudgeLabel = tk.Label(playerFrame, text="You are not the judge. Wait for the judge to select a card", wraplength=300,
                             justify="center", borderwidth=2)

    #sets the spaces for the meme card
    img = ImageTk.PhotoImage(mCard.getImage().resize(MEMECARDSIZE))
    memeCardLabel = tk.Label(playerFrame, image=img)
    memeCardLabel.image = img
    memeCardLabel.place(relx=0.5, rely=0.5, anchor="center")

    #event handlers for a player's cards. need to implement sending the card chosen by the judge to the server
    #and increment points of player who won the round
    def Card1ClickEvent(event):
        card2Label.destroy()
        root.update()
        sendResult(pCards[0])

    def Card2ClickEvent(event):
        card1Label.destroy()
        root.update()
        sendResult(pCards[1])

    def sendResult(pCard):
        if not client.sendRoundWinner(pCard.getPlayerName()):
            GUI.showLossGUI()
        else:
            sleep(1)
            GUI.showPlayerGUI(player.getUsername())

    def waitForNewRound():
        while not client.checkIfReadyForNewRound():
            sleep(1)
        if not client.isGameOver():
            GUI.showPlayerGUI(player.getUsername())
        elif player.getPoints() == "5":
            GUI.showWinGUI()
        else:
            GUI.showLossGUI()

    if player.isJudge():
        card1Label.bind("<Button-1>", Card1ClickEvent)
        card2Label.bind("<Button-1>", Card2ClickEvent)
        judgeLabel.place(height=50, width=300, relx=0.5, y=150,  rely=0.5, anchor="center")
    else:
        notJudgeLabel.place(height=50, width=300, relx=0.5, y=150, rely=0.5, anchor="center")
        root.after(1000, waitForNewRound)

    #returns the frame
    return playerFrame