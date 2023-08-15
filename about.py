from tkinter import *
import platform

AboutWindow = Tk()  # Fenêtre "A propos"
Dev = Label(AboutWindow, text = "Développeur : Terenceithaque") # Label d'info sur le développeur*
Dev.pack(side = TOP)
Platform = Label(AboutWindow, text = "Système d'exploitation : {}".format(platform.system()))
Platform.pack(side = TOP)


def OpenAboutWindow():
    if __name__ == "__main__":
        AboutWindow.mainloop()