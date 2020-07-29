import tkinter as tk
from PIL import ImageTk

#creates the in-game judging GUI. Takes in a list of 3 PhraseCards (1 from each player) and a MemeCard
def createPlayerMenu(root, pCards, mCard, isPlayerJudge):
    MEMECARDSIZE = (200, 200)

    #creates the frame for the in-game judging GUI
    playerFrame = tk.Frame(root, height=500, width=600)

    #sets the spaces for the players' chosen cards
    card1Label = tk.Label(playerFrame, text=pCards[0].getText(), wraplength=150, justify="center", borderwidth=2, relief="groove")
    card1Label.place(height=50, width=150, x=-200, relx=0.5, y=200, rely=0.5, anchor="center")
    card2Label = tk.Label(playerFrame, text=pCards[1].getText(), wraplength=150, justify="center", borderwidth=2, relief="groove")
    card2Label.place(height=50, width=150, relx=0.5, y=200,  rely=0.5, anchor="center")
    card3Label = tk.Label(playerFrame, text=pCards[2].getText(), wraplength=150, justify="center", borderwidth=2, relief="groove")
    card3Label.place(height=50, width=150, x=200, relx=0.5, y=200, rely=0.5, anchor="center")

    #sets the spaces for the meme card
    img = ImageTk.PhotoImage(mCard.getImage().resize(MEMECARDSIZE))
    memeCardLabel = tk.Label(playerFrame, image=img)
    memeCardLabel.image = img
    memeCardLabel.place(relx=0.5, rely=0.5, anchor="center")

    #event handlers for a player's cards. need to implement sending the card chosen by the judge to the server
    #and increment points of player who won the round
    def Card1ClickEvent(event):
        print("Clicked card 1")
        card2Label.destroy()
        card3Label.destroy()

    def Card2ClickEvent(event):
        print("Clicked card 2")
        card1Label.destroy()
        card3Label.destroy()

    def Card3ClickEvent(event):
        print("Clicked card 3")
        card1Label.destroy()
        card2Label.destroy()

    if isPlayerJudge:
        card1Label.bind("<Button-1>", Card1ClickEvent)
        card2Label.bind("<Button-1>", Card2ClickEvent)
        card3Label.bind("<Button-1>", Card3ClickEvent)

    #returns the frame
    return playerFrame