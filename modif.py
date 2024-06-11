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
HAUTEURGRADATION=40
MARGECOTE = 40
DIFGRADATIONTEXTE=5
LARGEURGRAD=MWIDTH

# edition
COTECASEPALETTE=LARGEURCASE*2
HAUTEUREDITION=COTECASEPALETTE*2

WIDTH = LARGEURCASE*48+MWIDTH*49 + MARGECOTE*2 
HEIGHT = HAUTEURCASE + MHEIGHT*2 +HAUTEURTEXTE + HAUTEURGRADATION + DIFGRADATIONTEXTE+HAUTEUREDITION


# TABVIERGE BOUTON

taille=(50,3)
tabvierge = np.zeros(taille)
tabvierge[49,1]=255
save_file_path_tabvierge = None

# Permet de sauvegarder le fichier tabvierge avec le nom donnée en entrée
def save_tabvierge(name) :
    np.savetxt(name,tabvierge)

# Utilisé pour le bouton enregistrer sous du tabvierge
def save_new_file_tabvierge():
    global save_file_path_tabvierge
    save_file_path =  filedialog.asksaveasfilename(initialdir = "/",title = "Select a day programme",filetypes = (("txt files","*.txt"),("all files","*.*")))
    if save_file_path :
        save_file_path_tabvierge= save_file_path
        save_tabvierge(save_file_path_tabvierge)

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
        reinitialiserbarre()

# Importation d'un fichier tabvierge à modifier
def import_file_tabvierge():
    global save_file_path_tabvierge
    file_path = filedialog.askopenfilename(title="Select a day programme", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path :
		# Process the selected file (you can replace this with your own logic)
        save_file_path_tabvierge=file_path
        impor_tabvierge(file_path)


# COLORPALETTE
TAILLE_PALETTE=10
taille = (TAILLE_PALETTE,3)
colorpalette = np.zeros(taille)
save_file_path_colorpalette = "default_color_palette.txt"
ERASER = np.array([0,0,0])

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
    save_colorpalette(save_file_path_colorpalette)

# importe une colorpalette dont le nom est donnee en intro
def impor_colorpalette(file_path) :
    tab = np.loadtxt(file_path)
    global colorpalette
    taille=(TAILLE_PALETTE,3)
    if (tab.shape != taille) : 
        return
    else : 
        print(tab)
        colorpalette = tab
        

# Importation d'un fichier colorpalette à modifier
def import_file_colorpalette():
    global save_file_path_colorpalette
    file_path = filedialog.askopenfilename(title="Select a colour palette", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path :
		# Process the selected file (you can replace this with your own logic)
        save_file_path_colorpalette=file_path
        impor_colorpalette(file_path)


# GESTION DE LA COULEUR SELECTIONNER

COULEURACTUEL=np.array([0,0,0])

def setcouleur(index) : 
    for i in range(0,3,1) :
        COULEURACTUEL[i]=colorpalette[index,i]
    print("couleur selectionner : ",COULEURACTUEL)

def setcase(index) : 
    print("bouton")
    for i in range(0,3,1) :
        tabvierge[index,i]=COULEURACTUEL[i]

# INITIALISATION DE LA FENETRE
root = tk.Tk()
root.configure(background='#263D42')
root.title("Day programme modifier ")
canvas = tk.Canvas(root,width=WIDTH,height=HEIGHT,bg="#263D42",highlightthickness=0)
canvas.grid(columnspan=3,row=0)
root.resizable(False,False)


# Liste rectangle coloré
LISTERECTANGLE=[]
LISTERECTANGLEPALETTE=[]

# GRAPHISME DE LA FENETRE

def reinpalettecouleur():
    for i in range(0,TAILLE_PALETTE,1):
        c = Color(rgb=(colorpalette[i,0]/255,colorpalette[i,1]/255,colorpalette[i,2]/255))
        color = "%s" %(c.hex)
        canvas.itemconfig(LISTERECTANGLEPALETTE[i], fill=color) 

def dessinerbarreindex(index) :
    if (tabvierge[index,0]==0 and tabvierge[index,1]==0 and tabvierge[index,2]==0) :
        at=48
    else :
        at=index
    c = Color(rgb=(tabvierge[at,0]/255,tabvierge[at,1]/255,tabvierge[at,2]/255))
    color = "%s" %(c.hex)
    canvas.itemconfig(LISTERECTANGLE[index], fill=color)

# redessine toutes les barres du programme
def reinitialiserbarre() :
    for i in range(0,50,1) :
        dessinerbarreindex(i)
        
# MODIFICATION DU PROGRAMME (BOUTON)
def inputprogramme(event) :
    for index in range(0,48,1) :
        departx=index*(LARGEURCASE+MWIDTH) + MARGECOTE 
        if ((event.x >= departx) and (event.x <= departx+LARGEURCASE)) :
            setcase(index)
            dessinerbarreindex(index)


def inputcouleurremplissage(_) :
    setcase(49)
    dessinerbarreindex(49)

def inputcouleurarriereplan(_) :
    setcase(48)
    dessinerbarreindex(48)
    reinitialiserbarre()

def inputcolorpalette(event) :
    for index in range(0,TAILLE_PALETTE,1) :
        departx=index*(COTECASEPALETTE*2) + COTECASEPALETTE*5
        if ((event.x >= departx) and (event.x <= departx+COTECASEPALETTE)) :
            setcouleur(index)

def inputeraser() :
    for i in range(0,3,1) :
        COULEURACTUEL[i]=ERASER[i]
    print("couleur selectionner : ",COULEURACTUEL)


# initialise les boutons et les graphisùe de l'interface
def init() :
    departy=MHEIGHT+HAUTEURTEXTE + HAUTEURGRADATION + DIFGRADATIONTEXTE
    # Création des différents rectangle de couleur du programme
    for index in range(0,48,1) : 
        c = Color(rgb=(tabvierge[index,0]/255,tabvierge[index,1]/255,tabvierge[index,2]/255))
        color = "%s" %(c.hex)
        departx=index*(LARGEURCASE+MWIDTH) + MARGECOTE
        LISTERECTANGLE.append(canvas.create_rectangle(departx,departy,departx+LARGEURCASE,departy+HAUTEURCASE,fill=color,outline=""))
    # Creation bouton pour la modification du programme
    rectangle = canvas.create_rectangle(MARGECOTE,departy,48*(LARGEURCASE+MWIDTH) + MARGECOTE,departy+HAUTEURCASE,fill="",outline="")
    canvas.tag_bind(rectangle,'<Button-1>',inputprogramme)
    departy=MHEIGHT+HAUTEURTEXTE + HAUTEURGRADATION + DIFGRADATIONTEXTE+COTECASEPALETTE//2 +HAUTEURCASE
    # AJOUT TEXTE selection couleur
    text=tk.Label(canvas,text="Color selector :",fg="white",bg="#263D42")
    text.place(relx = 0.07, 
                   rely = 0.8,
                   anchor = 'center')
    # Création des rectangles pour la selection des couleurs sur la palette de couleur
    for index in range(0,TAILLE_PALETTE,1) : 
        c = Color(rgb=(colorpalette[index,0]/255,colorpalette[index,1]/255,colorpalette[index,2]/255))
        color = "%s" %(c.hex)
        departx=index*(COTECASEPALETTE*2) + COTECASEPALETTE*5
        LISTERECTANGLEPALETTE.append(canvas.create_rectangle(departx,departy,departx+COTECASEPALETTE,departy+COTECASEPALETTE,fill=color,outline=""))
    # creation bouton interraction avec la palette de couleur
    rectangle = canvas.create_rectangle(COTECASEPALETTE,departy,10*(COTECASEPALETTE*2) + COTECASEPALETTE*5,departy+COTECASEPALETTE,fill="",outline="")
    canvas.tag_bind(rectangle,'<Button-1>',inputcolorpalette)
    # AJOUT BOUTON suppression
    bouton=tk.Button(canvas,text="Eraser",command=inputeraser)
    bouton.place(relx = 0.7, 
                   rely = 0.8,
                   anchor = 'center')
    # ajout texte background color
    text=tk.Label(canvas,text="Background :",fg="white",bg="#263D42")
    text.place(relx = 0.78, 
                   rely = 0.8,
                   anchor = 'center')
    # Ajout couleur d'arrière plan
    c = Color(rgb=(tabvierge[48,0]/255,tabvierge[48,1]/255,tabvierge[48,2]/255))
    color = "%s" %(c.hex)
    departy=MHEIGHT+HAUTEURTEXTE + HAUTEURGRADATION + DIFGRADATIONTEXTE+COTECASEPALETTE//2 +HAUTEURCASE
    departx=COTECASEPALETTE*30
    rectangle = canvas.create_rectangle(departx,departy,departx+COTECASEPALETTE,departy+COTECASEPALETTE,fill=color,outline="")
    canvas.tag_bind(rectangle,'<Button-1>',inputcouleurarriereplan)
    LISTERECTANGLE.append(rectangle)
    # AJOUT TEXTE couleur par defaut
    text=tk.Label(canvas,text="Progression :",fg="white",bg="#263D42")
    text.place(relx = 0.9, 
                   rely = 0.8,
                   anchor = 'center')
    #AJOUT COULEUR DE REMPLISSAGE
    c = Color(rgb=(tabvierge[49,0]/255,tabvierge[49,1]/255,tabvierge[49,2]/255))
    color = "%s" %(c.hex)
    departy=MHEIGHT+HAUTEURTEXTE + HAUTEURGRADATION + DIFGRADATIONTEXTE+COTECASEPALETTE//2 +HAUTEURCASE
    departx=COTECASEPALETTE*34 + 10
    rectangle = canvas.create_rectangle(departx,departy,departx+COTECASEPALETTE,departy+COTECASEPALETTE,fill=color,outline="")
    canvas.tag_bind(rectangle,'<Button-1>',inputcouleurremplissage)
    LISTERECTANGLE.append(rectangle)
    
    # BOUTON IMPORT
    import_button = tk.Button(root, text="import", command=import_file_tabvierge)
    import_button.grid(column=0,row=1)

    # BOUTON SAVE AS
    import_button = tk.Button(root, text="Save file as...", command=save_new_file_tabvierge)
    import_button.grid(column=1,row=1)

    # BOUTON FAST SAVE
    import_button = tk.Button(root, text="Save", command=save_file_tabvierge)
    import_button.grid(column=2,row=1)

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

impor_colorpalette(save_file_path_colorpalette)
setcouleur(0)
init()
graduation()
root.mainloop()
