from tkinter import *
from sauvegarde_ import nouvelle_sauvegarde, verif_sauvegarde, verifpseudo
from pdf_opener import open_given_pdf

#Création de la fenètre de bas
root = Tk()
root.geometry("1000x600")
root.config(bg="black")
root.minsize(1000,600)
root.maxsize(1000,600)

#Permet de reset une page sans la détruire
widget_lst: list = []
def destroy_widgets() -> None: 
    """Permet de détruire tous les widgets de la fenetre actuelle"""
    for widget in widget_lst:
        widget.destroy()

def start_menu() -> None:
    """Creer le menu de démarrage"""
    root.title("Authentification")
    #On reset la fenètre
    destroy_widgets()

    #On créé des widgets
    txt = Label(text="Inserer un nom de logiciel", bg="Black", fg="White", font=("Arial", 20))
    btn_quitter = Button(text="Quitter", command=root.destroy)
    btn_connect = Button(text="     Connection     ", command=connection_menu, font=("Arial", 17))
    btn_create = Button(text=" Créer un compte ", command=lambda:connection_menu('create'), font=("Arial", 17))

    #On récupère les widgets dans la liste afin de pouvoir les détruire
    widget_lst.append(btn_connect)
    widget_lst.append(btn_quitter)
    widget_lst.append(btn_create)
    widget_lst.append(txt)

    #On fait apparaître les widgets sur l'écran
    txt.pack(pady=50)
    btn_connect.pack(pady=100)
    btn_create.pack(pady=0)
    btn_quitter.pack(side=BOTTOM, fill=X)

    root.mainloop()
    
def connection_menu(menu:str = 'load') -> None:
    """Creer le menu de connection (soit connection soit charger)"""
    #On reset la fenètre
    destroy_widgets()
    
    def entry_load() -> None:
        """systeme de verification d'une sauvegarde à charger"""
        pseudo = pseudo_joueur.get() #On récupère le pseudo et le mdp
        mdp = mdp_joueur.get()
        erreur = verif_sauvegarde(str(pseudo), str(mdp), 'csvfile.csv') #on verrifie si le pseudo existe déjà
        if erreur == True: #dans le cas d'une erreur
            error_text.config(fg='red', text= "Le nom d'utilisateur ou mot de passe est incorrect !")
            error_text.pack(pady=2)
        else:
            menu_principal()

    def entry_create() -> None: 
        """systeme de verification/creation d'une nouvelle sauvegarde"""
        pseudo = pseudo_joueur.get()#On récupère le pseudo et le mdp
        mdp = mdp_joueur.get()
        verification = verifpseudo(pseudo, 'csvfile.csv')
        if verification == True:#dans le cas d'une erreur
            error_text.config(fg ='red', text='Ce pseudo existe déjà !')
        else:
            if len(pseudo) == 0:
                error_text.config(fg='red',  text = "Vous devez utiliser un mot de passe et un pseudo")
            else:
                nouvelle_sauvegarde(pseudo, mdp, 'csvfile.csv')
                menu_principal()
    
    #On créé les widgets puis on les récupère dans la liste afin de pouvoir les détruire
    label_titel = Label(root, font = ("Helvetica", 20), bg = 'black', fg='white')
    widget_lst.append(label_titel)

    label_pseudo = Label(root, text = "Votre Pseudo:", font = ("Helvetica", 20),bg = 'black', fg='white')
    widget_lst.append(label_pseudo)

    pseudo_joueur = Entry(root,font = ("Helvetica", 20), bg="black", fg='white', insertbackground='white', width=30)
    widget_lst.append(pseudo_joueur)

    label_mdp = Label(root, text = "Mot de Passe:", font = ("Helvetica", 20), bg="black", fg='white')
    widget_lst.append(label_mdp)

    mdp_joueur = Entry(root,font = ("Helvetica", 20),bg ='black', fg='white', insertbackground='white', width=30)
    widget_lst.append(mdp_joueur)

    error_text = Label(root, text="message erreur", font = ("Helvetica", 20), bg="black", fg='black')
    widget_lst.append(error_text)

    entrer_button = Button(root, text= 'Entrer',font = ("Helvetica", 20))
    widget_lst.append(entrer_button)

    btn_retour = Button(text="Retour", command=start_menu)
    widget_lst.append(btn_retour)
    
    #Permet la modification entre le menu de connection et de création de compte
    if menu=='create':  #Menu création compte
        root.title("Création d'un compte")
        label_titel.config(text="Veuillez créer un compte:")
        label_pseudo.config(text='Votre pseudo (original):')
        entrer_button.config(command=entry_create)
    else:   #Menu connection
        root.title('Connection')
        label_titel.config(text='Veuillez vous identifier:')
        entrer_button.config(command=entry_load)
    
    #On fait apparaître les widgets sur l'écran
    label_titel.pack(pady=25)
    label_pseudo.pack()
    pseudo_joueur.pack( pady=10)
    label_mdp.pack()
    mdp_joueur.pack(pady= 10)
    error_text.pack(pady=2)
    entrer_button.pack(pady=10)
    btn_retour.pack(side=BOTTOM, fill=X)

def menu_principal() -> None:
    """On créé la fenêtre du menu principal"""
    #On reset la fenètre
    destroy_widgets()
    root.title("Menu Principal")
    destroy_widgets()

    #On créé les widgets
    txt = Label(text="Menu principal", bg="Black", fg="White", font=("Arial", 20))
    btn_quitter = Button(text="Quitter", command=root.destroy)
    btn_connect = Button(text="Chapitres", command=chapitres, font=("Arial", 17))
    btn_account = Button(text='Compte (pour le moment ne sert a rien)', font=("Arial", 17))

    #On récupère les widgets dans la liste afin de pouvoir les détruire
    widget_lst.append(btn_connect)
    widget_lst.append(btn_account)
    widget_lst.append(btn_quitter)
    widget_lst.append(txt)

    #On fait apparaître les widgets sur l'écran
    txt.pack(pady=50)
    btn_account.place(anchor=NW)
    btn_connect.pack(pady=100)
    btn_quitter.pack(side=BOTTOM, fill=X)
    
def chapitres() -> None:
    """On créé la fentêtre pour accéder aux chapitres"""
    root.title("Chapitres")
    #On reset la fenètre
    destroy_widgets()

    #On créé les widgets
    txt = Label(text="Accéder au cours & exos", bg="Black", fg="White", font=("Arial", 20))
    btn_retour = Button(text="Retour", command=menu_principal)
    btn_connect = Button(text="Cours", command=cours, font=("Arial", 17))
    btn_create = Button(text="Exercice", command=exercice, font=("Arial", 17))

    #On récupère les widgets dans la liste afin de pouvoir les détruire
    widget_lst.append(btn_connect)
    widget_lst.append(btn_retour)
    widget_lst.append(btn_create)
    widget_lst.append(txt)

    #On fait apparaître les widgets sur l'écran
    txt.pack(pady=50)
    btn_connect.pack(pady=100)
    btn_create.pack(pady=0)
    btn_retour.pack(side=BOTTOM, fill=X)

def cours() -> None:
    """On créé la fenêtre pour accéder aux cours en PDF"""
    #On reset la fenètre
    destroy_widgets()
    root.title("Cours")

    #On créé les widgets
    btn_retour = Button(text="Retour", command=chapitres)
    btn_open_pdf = Button(text="Un pdf random",command=lambda:open_given_pdf("ouverture.pdf"))

    #On récupère les widgets dans la liste afin de pouvoir les détruire
    widget_lst.append(btn_retour)
    widget_lst.append(btn_open_pdf)

    #On fait apparaître les widgets sur l'écran
    btn_open_pdf.pack(pady=100)
    btn_retour.pack(side=BOTTOM, fill=X)

def exercice() -> None:
    """On créé la fenêtre pour accéder aux exercices en PDF"""
    #On reset la fenètre
    destroy_widgets()
    root.title("Exercices")
    btn_retour = Button(text="Retour", command=chapitres)
    btn_open_pdf = Button(text="Un pdf random",command=lambda:open_given_pdf("ouverture.pdf"))

    #On récupère les widgets dans la liste afin de pouvoir les détruire
    widget_lst.append(btn_retour)
    widget_lst.append(btn_open_pdf)

    #On fait apparaître les widgets sur l'écran
    btn_open_pdf.pack(pady=100)
    btn_retour.pack(side=BOTTOM, fill=X)

#On lance l'application au menu de démarrage
start_menu()