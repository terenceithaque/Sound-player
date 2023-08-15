# Programme qui permet l'import et la lecture de fichiers audio
import tkinter.filedialog
from tkinter import *
from tkinter import messagebox
from jouer_url import *
import vlc


is_playing = False

def BrowseFile():
    "Chercher un fichier audio puis le jouer"
    try:
        file =  tkinter.filedialog.askopenfilename(initialdir = "E:", title = "Importer un fichier audio", filetypes = (("Fichier audio", ".mp3"), ("all files", "*.*")))
    except:
        file = tkinter.filedialog.askopenfilename(initialdir = "C:", title = "Importer un fichier audio", filetypes = (("Fichier audio", ".mp3"), ("all files", "*.*")))

    print(file)

    def PlayAudio():
        "Jouer le fichier sélectionné par l'utilisateur"
        try:
            global media
            media = vlc.MediaPlayer(file)
            media.play()
        except:
            messagebox.showerror("Erreur de lecture d'un fichier", "Une erreur s'est produite lors de la lecture du fichier '{}'; peut-être devriez vous réessayer. Si le lecteur sur lequel ce fichier se trouve est externe, vous devriez essayer de réinsérer ce lecteur, puis recommencer.".format(file))    
    def changeButtonText():
        new_text = BoutonImporter.configure(text = "Ecoute terminée ({})".format(file))
        fen.title("{} - Sound Player".format(file))
        print(new_text)
    changeButtonText() 
    PlayAudio()


def play_pause_media():
    "Permettre à l'utilisateur de mettre en pause ou de reprendre la lecture"
    global is_playing

    if 'media' not in globals():
        messagebox.showerror("Erreur de lecture", "Aucun fichier audio n'a été sélectionné.")
        return

    if is_playing == False:
        media.set_pause(1)
        BoutonPause.config(text="Reprendre la lecture")
        is_playing = True
    else:
        media.set_pause(0)
        BoutonPause.config(text="Pause")
        is_playing = False





   




def about():
    messagebox.showinfo("Sound Player", "Sound Player est un programme minimaliste permettant de lire des fichiers audio.")
  

def StopRun():
    "Quitter le programme"
    print(is_playing)
    if is_playing == False:
        ask_quit = messagebox.askquestion("Quitter en cour de lecture", "Voulez-vous vraiment quitter en cour de lecture ?")
        if ask_quit == "yes":

            fen.destroy()
    
    elif is_playing == True:
        fen.destroy()        

   

  



fen = Tk()
fen.title("Sound Player")
descr = Label(fen, text = "Importer un fichier audio et lisez le") # Description du programme
#descr.pack(side = TOP)
BoutonImporter = Button(fen, text = "Chercher un fichier audio et le jouer", command = BrowseFile)
BoutonImporter.pack(side = TOP)
BoutonUrl = Button(fen, text = "Jouer un fichier (URL)", command= lambda:creer_fenetre_saisir_url(fen))
BoutonUrl.pack(side = TOP)
BoutonPause = Button(fen, text = "Pause", command = play_pause_media)
BoutonPause.pack(side = TOP)
BoutonPropos = Button(fen, text = "A propos...", command = about)
BoutonPropos.pack(side = TOP)
BoutonPropos.pack(side = TOP)
BoutonQuitter = Button(fen, text = "Quitter", command = StopRun) # Arrêter proprement l'exécution du programme
BoutonQuitter.pack(side = TOP)
#BoutonJouer = Button(fen, text = "Jouer le fichier importé", command = PlayAudio)
#BoutonJouer.pack(side = TOP)

if __name__ == '__main__':
  fen.mainloop()


