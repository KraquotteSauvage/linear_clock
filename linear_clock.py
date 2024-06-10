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
HAUTEURGRADATION=30
MARGECOTE = 40
DIFGRADATIONTEXTE=5
LARGEURGRAD=MWIDTH
WIDTH = LARGEURCASE*48+MWIDTH*49 + MARGECOTE*2 + LARGEURBOUTON
HEIGHT = HAUTEURCASE + MHEIGHT*2 +HAUTEURTEXTE + HAUTEURGRADATION + DIFGRADATIONTEXTE

taille = (48,3)
tabactuel = np.zeros(taille)
taille=(50,3)
tabvierge = np.zeros(taille)
tabvierge[49,1]=255
LISTERECTANGLE=[]

# Fonction qui import le fichier
def impor(file_path) :
    tab = np.loadtxt(file_path)
    global tabvierge
    taille=(50,3)
    if (tab.shape != taille) : 
        return
    else : 
        tabvierge = tab
        tabatemps()
        reinbarre()

# Fonction pour import avec le bouton import
def import_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path :
		# Process the selected file (you can replace this with your own logic)
        impor(file_path)
        
	    
root = tk.Tk()
root.title("Linear clock")
root.configure(background='#263D42')
#root.attributes('-alpha', 0.3) modifiable avec un bouton = bonne idée
#root.overrideredirect(1) à réfléchir avec un boolean
canvas = tk.Canvas(root,width=WIDTH,height=HEIGHT,bg="#263D42",highlightthickness=0)
canvas.grid(row=0,columnspan=5)
root.resizable(False,False)
PLEINE_ECRAN=tk.BooleanVar()

# Bouton pour prioriser l'écran
def boutonprioriseecran():
    root.attributes("-topmost", PLEINE_ECRAN.get())

# Permet de savoir si un crénaux du programme est vide
def compare(index) : 
    for i in range(3) : 
        if tabvierge[index,i]!=0 : 
            return False
    return True

# Met à jour la tabactuel qui est utilisé dans l'affichage et renvoie l'index correspondant à la tranche horaire actuel
def tabatemps() : 
    temps=tm.localtime(tm.time())
    point = temps.tm_hour*2+1
    point += temps.tm_min // 30
    for i in range(0,point,1) : 
        if compare(i) : 
            tabactuel[i]=tabvierge[49]
        else : 
            tabactuel[i]=tabvierge[i]
    for i in range(point,48,1) :
        tabactuel[i]=tabvierge[48]
    return point-1

# Créer un programme vide à l'allumage du programme
def debase(couleurRien,couleurPassee) :
    # tab 48 = quand vide
    # tab 49 = quand déjà finis mais R
    for i in range(3) : 
        tabvierge[48,i]=couleurRien[i]
        tabvierge[49,i]=couleurPassee[i]

# Recolore le rectangle à un index précis
def dessinerbarreindex(index) :
    c = Color(rgb=(tabactuel[index,0]/255,tabactuel[index,1]/255,tabactuel[index,2]/255))
    color = "%s" %(c.hex)
    canvas.itemconfig(LISTERECTANGLE[index], fill=color)

# recolore toutes les barres verticales du programmes
def reinbarre() :
    for i in range(0,48,1) :
        dessinerbarreindex(i)

# Initialisation de la graduation à l'aide des rectangles
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

# Initialisation des rectangles du programmes de la journée
def initbarre() :
    departy=MHEIGHT+HAUTEURTEXTE + HAUTEURGRADATION + DIFGRADATIONTEXTE
    for i in range(0,48,1) : 
        c = Color(rgb=(tabactuel[i,0]/255,tabactuel[i,1]/255,tabactuel[i,2]/255))
        color = "%s" %(c.hex)
        departx=i*(LARGEURCASE+MWIDTH) + MARGECOTE
        LISTERECTANGLE.append(canvas.create_rectangle(departx,departy,departx+LARGEURCASE,departy+HAUTEURCASE,fill=color,outline=""))

# fonction de mise à jour de l'affichage
def maj() :
    dessinerbarreindex(tabatemps())
    canvas.after(30000,maj)

import_button = tk.Button(root, text="Import File", command=import_file)
import_button.grid(row=1,column=3,sticky='w')
bouton = tk.Checkbutton(root, text='Prioritise this window',variable=PLEINE_ECRAN, onvalue=True,offvalue=False, command=boutonprioriseecran)
bouton.grid(row=1,column=1,sticky='e')
# [R,G,B]
debase(np.array([0,0,0]),np.array([0,255,0]))
tabatemps()
graduation()
initbarre()
maj()
root.mainloop()