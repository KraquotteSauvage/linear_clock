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

taille = (48,3)
tabactuel = np.zeros(taille)
taille=(50,3)
tabvierge = np.zeros(taille)


def impor(file_path) :
    tab = np.loadtxt(file_path)
    global tabvierge
    taille=(50,3)
    if (tab.shape != taille) : 
        return
    else : 
        tabvierge = tab

def import_file():
    
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path :
		# Process the selected file (you can replace this with your own logic)
        impor(file_path)
	    
        

root = tk.Tk()
canvas = tk.Canvas(root,width=WIDTH,height=HEIGHT,bg="#263D42")
canvas.pack()

def compare(index) : 
    for i in range(3) : 
        if tabvierge[index,i]!=0 : 
            return False
    return True

def tabatemps() : 
    temps=tm.localtime(tm.time())
    point = temps.tm_hour*2+1
    point += temps.tm_min // 30
    print("point = ",point)
    for i in range(0,point,1) : 
        if compare(i) : 
            tabactuel[i]=tabvierge[49]
        else : 
            tabactuel[i]=tabvierge[i]
    for i in range(point,48,1) :
        tabactuel[i]=tabvierge[48]

def debase(couleurRien,couleurPassee) :
    # tab 48 = quand vide
    # tab 49 = quand déjà finis mais R
    for i in range(3) : 
        tabvierge[48,i]=couleurRien[i]
        tabvierge[49,i]=couleurPassee[i]

def setcase(index, couleur) : 
    tabvierge[index]=couleur

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


def dessinerbarre() :
    departy=MHEIGHT+HAUTEURTEXTE + HAUTEURGRADATION + DIFGRADATIONTEXTE
    for i in range(0,48,1) : 
        c = Color(rgb=(tabactuel[i,0],tabactuel[i,1],tabactuel[i,2]))
        color = "%s" %(c.hex)
        departx=i*(LARGEURCASE+MWIDTH) + MARGECOTE
        canvas.create_rectangle(departx,departy,departx+LARGEURCASE,departy+HAUTEURCASE,fill=color,outline="")


def maj() :
    tabatemps()
    dessinerbarre()
    canvas.after(10000,maj)

import_button = tk.Button(root, text="Import File", command=import_file)
import_button.pack()
# [R,G,B]
debase(np.array([0.1,0.1,0.1]),np.array([0.2,1,0.2]))
impor("default.txt")
graduation()
maj()
root.mainloop()