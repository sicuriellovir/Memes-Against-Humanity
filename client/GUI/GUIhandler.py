import tkinter as tk
import MainMenu as menu
import ReadyGUI as ready
import OptionsGUI as opt

root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)

menuFrame = menu.createMainMenu(root)
readyFrame = ready.createReadyMenu(root)

def showMainMenu():
    menuFrame.pack()
    root.mainloop()

def showReadyMenu():
    readyFrame.pack()
    root.mainloop()

def showOptionsWindow():
    opt.createOptionsWindow()

def exit():
    menuFrame.destroy()
    readyFrame.destroy()
    root.destroy()