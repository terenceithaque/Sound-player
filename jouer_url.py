# Jouer un fichier audio désigné par une URL fournie par l'utilisateur
from tkinter import *
import vlc
from urllib.parse import quote

def creer_fenetre_saisir_url(master):
    "Créer une nouvelle fenêtre pour saisir l'URL"
    fenetre_saisie_url = Toplevel(master)
    url_label = Label(fenetre_saisie_url, text= "URL du fichier:")
    url_label.pack()
    url_entry = Entry(fenetre_saisie_url)
    url_entry.pack()


    def jouer():
      url =  url_entry.get()
      media = vlc.MediaPlayer(url)

      media.play()

      master.title("{}-Sound Player".format(url)) 

      fenetre_saisie_url.destroy()





      


    bouton_jouer = Button(fenetre_saisie_url, text="Jouer le fichier", command = jouer)
    bouton_jouer.pack()    

