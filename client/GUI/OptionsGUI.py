import tkinter as tk

def createOptionsWindow():
    optionsWindow = tk.Tk()
    optionsWindow.geometry("200x100")

    tempLabel = tk.Label(optionsWindow, text="Not yet implemented")
    closeButton = tk.Button(optionsWindow, text="Exit")
    tempLabel.place(relx=0.5, rely=0.5, y=-20, anchor="center")
    closeButton.place(relx=0.5, rely=0.5, y=20, anchor="center")

    def closeEvent(event):
        closeButton.destroy()
        tempLabel.destroy()
        optionsWindow.destroy()
    closeButton.bind('<Button-1>', closeEvent)