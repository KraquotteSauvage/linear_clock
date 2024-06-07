import numpy as np
import time as tm
import tkinter as tk
from tkinter import filedialog
from colour import Color

MWIDTH = 6
MHEIGHT = 5
LARGEURCASE = 15
HAUTEURCASE = 50
HAUTEURTEXTE = 25
LARGEURBOUTON=0
HAUTEURGRADATION=40
MARGECOTE = 40
DIFGRADATIONTEXTE=5
LARGEURGRAD=MWIDTH
WIDTH = LARGEURCASE*48+MWIDTH*49 + MARGECOTE*2 + LARGEURBOUTON
HEIGHT = HAUTEURCASE + MHEIGHT*2 +HAUTEURTEXTE + HAUTEURGRADATION + DIFGRADATIONTEXTE


# TABVIERGE BOUTON

taille=(50,3)
tabvierge = np.zeros(taille)
save_file_path_tabvierge = None

# Permet de sauvegarder le fichier tabvierge avec le nom donnée en entrée
def save_tabvierge(name) :
    np.savetxt(name,tabvierge)

# Utilisé pour le bouton enregistrer sous du tabvierge
def save_new_file_tabvierge():
    global save_file_path_tabvierge
    save_file_path =  filedialog.asksaveasfilename(initialdir = "/",title = "Select a day programme",filetypes = (("txt files","*.txt"),("all files","*.*")))
    if save_file_path :
		# Process the selected file (you can replace this with your own logic)
        save_file_path_tabvierge=save_file_path
        save_tabvierge(save_file_path)

# enregistre tabvierge dans le fichier charger
def save_file_tabvierge() :
    global save_file_path_tabvierge
    if save_file_path_tabvierge!=None :
        save_tabvierge(save_file_path_tabvierge)

# importe une tabvierge dont le nom est donnee en intro
def impor_tabvierge(file_path) :
    tab = np.loadtxt(file_path)
    global tabvierge
    taille=(50,3)
    if (tab.shape != taille) : 
        return
    else : 
        tabvierge = tab

# Importation d'un fichier tabvierge à modifier
def import_file_tabvierge():
    global save_file_path_tabvierge
    file_path = filedialog.askopenfilename(title="Select a day programme", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path :
		# Process the selected file (you can replace this with your own logic)
        save_file_path_tabvierge=file_path
        impor_tabvierge(file_path)


# COLORPALETTE

taille = (10,3)
colorpalette = np.zeros(taille)
save_file_path_colorpalette = "default_color_palette.txt"

# Permet de sauvegarder la palette de couleur dont le nom est donnée en entrée
def save_colorpalette(name) : 
    np.savetxt(name,colorpalette)

# Utilisé pour le bouton enregistrer sous du colorpalette
def save_new_file_colorpalette():
    global save_file_path_colorpalette
    save_file_path =  filedialog.asksaveasfilename(initialdir = "/",title = "Select colour palette",filetypes = (("txt files","*.txt"),("all files","*.*")))
    if save_file_path :
		# Process the selected file (you can replace this with your own logic)
        save_file_path_colorpalette=save_file_path
        save_colorpalette(save_file_path)

# enregistre colopalette dans le fichier charger
def save_file_colopalette() :
    global save_file_path_colorpalette
    save_tabvierge(save_file_path_tabvierge)

# importe une colorpalette dont le nom est donnee en intro
def impor_colorpalette(file_path) :
    tab = np.loadtxt(file_path)
    global colorpalette
    taille=(10,3)
    if (tab.shape != taille) : 
        return
    else : 
        colorpalette = tab

# Importation d'un fichier colorpalette à modifier
def import_file_colorpalette():
    global save_file_path_colorpalette
    file_path = filedialog.askopenfilename(title="Select a colour palette", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path :
		# Process the selected file (you can replace this with your own logic)
        save_file_path_colorpalette=file_path
        impor_colorpalette(file_path)


root = tk.Tk()
canvas = tk.Canvas(root,width=WIDTH,height=HEIGHT,bg="#263D42")
canvas.pack()

def graduation() : 
    #F0F0F2 = gris
    # ajout de graduation basé sur l'affichage de l'image
    c1 = Color(rgb=(0.1,0.1,0.1))
    c2 = Color(rgb=(1,1,1))
    gris = "%s" %(c1.hex)
    blanc = "%s" %(c2.hex)
    departy=MHEIGHT
    finy=departy+HAUTEURGRADATION+HAUTEURTEXTE
    grandgrady= MHEIGHT+HAUTEURTEXTE
    minigrady= MHEIGHT+HAUTEURGRADATION//2+HAUTEURTEXTE
    for i in range(0,49,1) : 
        departx=i*(LARGEURCASE+MWIDTH) + MARGECOTE - LARGEURCASE//2 - MWIDTH//2
        canvas.create_rectangle(departx,departy,departx+LARGEURCASE,finy,fill=gris,outline="")
        #ajout des graduations
        departx=i*(LARGEURCASE+MWIDTH) + MARGECOTE - MWIDTH
        if (i%2==0) :
            gradactuel=grandgrady
            #ajout label
            num="%s" %(i//2)
            label=tk.Label(root,text=num,background=gris,foreground=blanc,width=2)
            label.place(x=departx-7,y=grandgrady-HAUTEURTEXTE)
        else :
            gradactuel=minigrady
        canvas.create_rectangle(departx,gradactuel,departx+LARGEURGRAD,finy,fill=blanc,outline="")


