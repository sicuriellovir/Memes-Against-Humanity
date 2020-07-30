import tkinter as tk
from .. import client
from . import GUIhandler as GUI
from PIL import ImageTk
from time import sleep

#creates the in-game player GUI. Takes in a list of 3 PhraseCards and a MemeCard
def createPlayerMenu(root, player, mCard):
    MEMECARDSIZE = (200, 200)

    #creates the frame for the in-game menu of a player
    playerFrame = tk.Frame(root, height=500, width=600)

    pCards = player.getPhraseCards()
    #sets the spaces for the current cards
    card1Label = tk.Label(playerFrame, text=pCards[0].getText(), wraplength=150, justify="center", borderwidth=2, relief="groove")
    card2Label = tk.Label(playerFrame, text=pCards[1].getText(), wraplength=150, justify="center", borderwidth=2, relief="groove")
    card3Label = tk.Label(playerFrame, text=pCards[2].getText(), wraplength=250, justify="center", borderwidth=2, relief="groove")
    judgeLabel = tk.Label(playerFrame, text="You are the judge. Wait for other players to select cards.", wraplength=150,
                          justify = "center", borderwidth = 2, relief = "groove")
    scoreLabel = tk.Label(playerFrame, text="Score: " + player.getPoints())
    scoreLabel.place(height=50, width=50, x=0, relx=0.5, y=150, rely=0.5, anchor="center")

    #sets the spaces for the meme card
    img = ImageTk.PhotoImage(mCard.getImage().resize(MEMECARDSIZE))
    memeCardLabel = tk.Label(playerFrame, image=img)
    memeCardLabel.image = img
    memeCardLabel.place(relx=0.5, rely=0.5, anchor="center")

    #event handlers for a player's cards. need to implement sending the card chosen by the player to the server
    def Card1ClickEvent(event):
        card2Label.destroy()
        card3Label.destroy()
        root.update()
        client.sendSelectedPhraseCard(pCards[0].getFileName())
        player.replaceCard(pCards[0])
        waitForJudgePhase()

    def Card2ClickEvent(event):
        card1Label.destroy()
        card3Label.destroy()
        root.update()
        client.sendSelectedPhraseCard(pCards[1].getFileName())
        player.replaceCard(pCards[1])
        waitForJudgePhase()

    def Card3ClickEvent(event):
        card1Label.destroy()
        card2Label.destroy()
        root.update()
        client.sendSelectedPhraseCard(pCards[2].getFileName())
        player.replaceCard(pCards[2])
        waitForJudgePhase()

    def waitForJudgePhase():
        client.setAsReadyForJudge()
        while not client.checkIfReadyToJudge():
            sleep(1)
        GUI.showJudgingGUI(player)

    if not player.isJudge():
        card1Label.place(height=50, width=150, x=-200, relx=0.5, y=200, rely=0.5, anchor="center")
        card2Label.place(height=50, width=150, x=0, relx=0.5, y=200, rely=0.5, anchor="center")
        card3Label.place(height=50, width=150, x=200, relx=0.5, y=200, rely=0.5, anchor="center")
        card1Label.bind("<Button-1>", Card1ClickEvent)
        card2Label.bind("<Button-1>", Card2ClickEvent)
        card3Label.bind("<Button-1>", Card3ClickEvent)
    else:
        judgeLabel.place(height=50, width=250, x=0, relx=0.5, y=200, rely=0.5, anchor="center")
        root.after(1000, waitForJudgePhase)

    #returns the frame
    return playerFrame