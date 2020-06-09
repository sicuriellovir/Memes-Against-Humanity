import tkinter as tk
import MainMenu as menu
import ReadyGUI as ready
import OptionsGUI as opt
#creates the main window with size 300x300 and makes it non-resizable
root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)

#gets the frames that can be stored in the window (just main menu and ready menu at this point)
menuFrame = menu.createMainMenu(root)
readyFrame = ready.createReadyMenu(root)

#sets the menu frame in the window
def showMainMenu():
    menuFrame.pack()
    root.mainloop()

#sets the ready frame in the window
def showReadyMenu():
    readyFrame.pack()
    root.mainloop()

#creates a seperate window for the options
def showOptionsWindow():
    opt.createOptionsWindow()

#runs when the program exist. Doesn't end the program, just deletes the window and its frames
def exit():
    menuFrame.destroy()
    readyFrame.destroy()
    root.destroy()