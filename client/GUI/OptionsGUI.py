import tkinter as tk

def createOptionsWindow():
    #creates the options window with size 200x100 and makes it non-resizable
    optionsWindow = tk.Tk()
    optionsWindow.geometry("200x100")
    optionsWindow.resizable(False, False)

    #creates a label and a button and sets their positions. Label is temporary, will add options later
    tempLabel = tk.Label(optionsWindow, text="Not yet implemented")
    closeButton = tk.Button(optionsWindow, text="Exit")
    tempLabel.place(relx=0.5, rely=0.5, y=-20, anchor="center")
    closeButton.place(relx=0.5, rely=0.5, y=20, anchor="center")

    #runs if the user clicks "Exit"
    def closeEvent(event):
        closeButton.destroy()
        tempLabel.destroy()
        optionsWindow.destroy()
    closeButton.bind('<Button-1>', closeEvent)
