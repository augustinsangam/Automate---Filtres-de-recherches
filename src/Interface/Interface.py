####################################################################################
#   Fichier     :   Interface.py
#   Auteur      :   EyaTom Augustin SANGAM & AbdelRahman Mohammed Bassiouni 
#                       & Nicolas Verbaere
#   Date        :   28 Novembre 2019
#   Projet      :   Automate : Filtres de recherches
####################################################################################

from tkinter                                        import ttk
from tkinter                                        import *
from tkinter                                        import messagebox
from Etat                                           import Etat
from Automate                                       import Automate
from Panier                                         import Panier
from Interface.CommandeImpossibleError              import CommandeImpossibleError
import os.path


class Interface(Frame) :
    """
    Classe Interface

    Classe utilisé pour l'affichage de l'interface. On utilise la bibliotèque tkinter
    qui est destiné à créer des interfaces graphiques.
    """

    def __init__(self):
        """
        Constructueur

        """

        self.fenetrePrincipale  =   Tk()
        self.canvasPrincipale   =   None        #le widget principale.
        self.canvasCommande     =   None
        self.initialiserGUI()                   #Place les bouttons sur la page d'acceuil
        self.automate           =   None
        self.panier             =   Panier()
        self.fenetrePrincipale.resizable(0, 0)


    def initialiserGUI(self, **kwargs):
        """ 
        Fonction qui initialise l'affichage de l'acceuil (au niveau des titres et des dimensions)

        paramètres      liste de widget fournis par la librairie
        """

        Frame.__init__(self, self.fenetrePrincipale, **kwargs)
        self.pack(fill=BOTH)
        self.master.title('Livraison')

        self.canvasPrincipale = Canvas(self.fenetrePrincipale, width=1400, height=650, background='white')
        self.canvasCommande   = Canvas(self.fenetrePrincipale, width=600, height=450, background='#e6f2ff',borderwidth=5, relief=RAISED)
        self.canvasPanier     = Canvas(self.fenetrePrincipale, width=350, height=450, background='#ffe6e6',borderwidth=5, relief=RAISED)


        self.canvasCommande.place(relx=0.43, rely=0.5, anchor=CENTER)
        self.canvasPanier.place(relx=0.83, rely=0.5, anchor=CENTER)


        self.canvasPrincipale.create_text(710, 30, text="Bienvenue dans notre système de livraison", font="Arial 32 bold",
                                          fill="black")

        self.canvasPrincipale.create_text(710, 640, text="@Verbaere Nicolas, Sangam Augustin, Abdelrahman Bassiouni", font="Arial 10 bold",
                                          fill="black")
        self.canvasPrincipale.create_text(110, 142, text="  Initialiser \nProgramme",
                                          font="Arial 20 bold",
                                          fill="black", tag="texteACacher")

        self.canvasPrincipale.create_text(110, 142, text="  Programme Initialisé",
                                          font="Arial 16 bold",
                                          fill="red", tag="programmeInitialise")
        self.canvasPrincipale.itemconfigure("programmeInitialise", state='hidden')

        self.insererBouttons()
        self.insererInputsCommande()
        self.insererInputPanier()


    def insererBouttons(self):
        """ 
        Fonction qui insere tous les bouttons de l'interface, et les relient à leurs méthodes
        """
        photo           = PhotoImage(file = r"../data/image/Play-Button.png")
        label           = Label(image=photo)
        label.image     = photo  # on garde une référence!
        bouttonImage    = Button(self.fenetrePrincipale,  image= label.image,command=self.creerAutomate, anchor=CENTER, cursor="hand2")
        bouttonImage.configure(width=150, height=150, activebackground="#33B5E5", cursor="hand2")


        self.canvasPrincipale.create_window(30, 265, anchor=W, window=bouttonImage, tag="imageACacher")
        self.canvasPrincipale.pack()


        bouttonAjouterPanier = Button(self.fenetrePrincipale, text="Ajouter au Panier", command=self.ajouterPanier, anchor=CENTER, cursor="hand2")
        bouttonAjouterPanier.configure(width=20, height=1, activebackground="#33B5E5", cursor="hand2", font="Arial 15 bold")
        self.canvasCommande.create_window(180, 400, anchor=W, window=bouttonAjouterPanier)


        bouttonCommander = Button(self.fenetrePrincipale, text="Commander", command=self.commander,
                                      anchor=CENTER, cursor="hand2")
        bouttonCommander.configure(width=20, height=1, activebackground="#33B5E5", cursor="hand2",
                                       font="Arial 15 bold")
        self.canvasPanier.create_window(180, 415, anchor = CENTER, window=bouttonCommander)


        bouttonRetirerPanier = Button(self.fenetrePrincipale, text="Retirer du Panier", command=self.retirerPanier,
                                 anchor=CENTER, cursor="hand2")
        bouttonRetirerPanier.configure(width=20, height=1, activebackground="#33B5E5", cursor="hand2", font="Arial 15 bold")
        self.canvasPanier.create_window(180, 295, anchor = CENTER, window=bouttonRetirerPanier)



        bouttonViderPanier = Button(self.fenetrePrincipale, text="Vider le Panier", command=self.viderPanier,
                                 anchor=CENTER, cursor="hand2")
        bouttonViderPanier.configure(width=20, height=1, activebackground="#33B5E5", cursor="hand2", font="Arial 15 bold")
        self.canvasPanier.create_window(180, 355, anchor=CENTER, window=bouttonViderPanier)


    def insererInputsCommande(self):
        """
        Fonction qui insere tous les widgets dans la section 'Inventaire'
        """

        self.canvasCommande.create_text(280, 30, text="     Inventaire", font="Arial 24 bold",
                                        fill="black")
        self.canvasCommande.create_text(63, 73, text="  Chosir le type", font="Arial 13 bold",
                                        fill="black")
        self.canvasCommande.create_text(263, 73, text="  Ecrire le code", font="Arial 13 bold",
                                        fill="black")
        self.canvasCommande.create_text(463, 73, text="  Ecrire le nom", font="Arial 13 bold",
                                        fill="black")


        self.comboBox = ttk.Combobox(self.fenetrePrincipale,
                                    values=['',
                                        "A",
                                        "B",
                                        "C"], width=12, state = "readonly")
        self.comboBox.place(relx=0.252, rely=0.29, anchor=CENTER)
        self.comboBox.current(0)
        self.comboBox.bind("<<ComboboxSelected>>", self.mettreAJourInventaire)


        self.inputCode = StringVar(self.fenetrePrincipale, value='')
        self.inputNom = StringVar(self.fenetrePrincipale, value='')

        self.inputCode.trace("w", lambda name, index, mode, inputCode=self.inputCode: callbackInput(self.inputCode))
        self.inputNom.trace("w", lambda name, index, mode, inputCode=self.inputNom: callbackInput(self.inputNom))

        def callbackInput(sv):
            self.mettreAJourInventaire()

        inputCodeWidget = Entry(self.fenetrePrincipale,textvariable=self.inputCode, borderwidth=2, width=14)
        inputNomWidget = Entry(self.fenetrePrincipale, borderwidth=2, textvariable=self.inputNom)
        inputCodeWidget.pack()
        inputNomWidget.pack()


        self.canvasCommande.create_window(215, 96, anchor=W, window=inputCodeWidget)
        self.canvasCommande.create_window(415, 96, anchor=W, window=inputNomWidget)


        frame = Frame(self.fenetrePrincipale)
        frame.place(relx=0.43, rely=0.53, anchor=CENTER)
        self.listeInventaire = Listbox(frame, width=60, font="Helvetica 12 ")
        self.listeInventaire.pack(side="left", fill="y")
        scrollbar = Scrollbar(frame, orient="vertical")
        scrollbar.config(command=self.listeInventaire.yview)
        scrollbar.pack(side="right", fill="y")
        self.listeInventaire.config(yscrollcommand=scrollbar.set)

        self.canvasCommande.create_text(140, 140, text=" 0 elements correspondant", font="Arial 13 bold",
                                        fill="black", tag="textLongeur")


    def insererInputPanier(self):
        """
        Fonction qui insere tous les widgets dans la section 'Panier'
        """

        self.canvasPanier.create_text(190, 30, text="Panier", font="Arial 24 bold",
                                      fill="black")
        self.canvasPanier.create_text(118, 64, text=" 0 kg dans le panier", font="Arial 13 bold",
                                        fill="black", tag="poidPanier")
        frame = Frame(self.fenetrePrincipale)
        frame.place(relx=0.83, rely=0.4, anchor=CENTER)

        self.listePanier = Listbox(frame, width=30, height=9, font=("Helvetica", 12))
        self.listePanier.pack(side="left", fill="y")

        scrollbar = Scrollbar(frame, orient="vertical")
        scrollbar.config(command=self.listePanier.yview)
        scrollbar.pack(side="right", fill="y")

        self.listePanier.config(yscrollcommand=scrollbar.set)


    def mettreAJourInventaire(self, event=None):
        """
        Fonction qui met à jour l' Inventaire
        """

        try:
            self.listeInventaire.delete(0, END)
            etat = Etat(self.inputNom.get(), self.inputCode.get(), self.comboBox.get())
            choixPossibles = self.automate.obtenirChoixPossibles(etat)
            for element in choixPossibles[1]:
                self.listeInventaire.insert(END, element.obtenirChaine())
            self.canvasCommande.itemconfig("textLongeur", text=" {} ".format(choixPossibles[0])+"elements correspondant(s)")

        except:
            pass

    def mettreAJOurPanier(self):

        """
        Fonction qui met à jour le panier
        """
        self.listePanier.delete(0, END)
        for element in self.panier:
            self.listePanier.insert(END, element.obtenirChaine())
        self.canvasPanier.itemconfig("poidPanier",
                                     text="{} ".format(self.panier.poids) + "kg dans le panier")

    def creerAutomate(self) :

        """
        Fonction qui creer l'Automate
        """
        master = Tk()
        master.geometry("260x80+200+200")
        master.title('Creer Automate')
        self.initialiserEntreeFichier(master)
        master.mainloop()
        master.destroy()



    def modifierTailleListes(self, estUnAjoutPanier, chaine, estUneCommande=False):
        """
        Fonction qui modifie la taille des listes pour le panier et pour l'inventaire
        """

        if(estUnAjoutPanier):
            try:
                self.panier += Etat(*chaine.split(" "))
                self.automate -= Etat(*chaine.split(" "))
            except CommandeImpossibleError:
                messagebox.showerror("Erreur",
                                     'Panier trop lourd !')

        else:
            self.panier -= Etat(*chaine.split(" "))
            if not estUneCommande:
                self.automate += Etat(*chaine.split(" "))
        self.mettreAJourInventaire()
        self.mettreAJOurPanier()


    def ajouterPanier(self):
        """
        Fonction qui ajoute l'élément séléctionner dans le panier
        """

        try:
            index = self.listeInventaire.curselection()[0]
            objet = self.listeInventaire.get(index)
            self.modifierTailleListes(True,objet)
        except IndexError:
            self.automateNonInitialiserErreur()


    def retirerPanier(self):
        """
        Fonction qui retire l'élément séléctionné du panier
        """
        try:
            index = self.listePanier.curselection()[0]
            objet = self.listePanier.get(index)
            self.modifierTailleListes(False,objet)
        except IndexError:
            self.automateNonInitialiserErreur()


    def viderPanier(self, estUneCommande=False):
        """
        Fonction qui vide le panier
        """
        try:
            self.automateNonInitialiserErreur()
            for element in self.listePanier.get(0,self.listePanier.size()-1):
                self.modifierTailleListes(False,element,estUneCommande)
        except IndexError:
            self.automateNonInitialiserErreur()

    def commander(self):
        """
        Fonction qui passe une commande
        """
        try:
            self.viderPanier(True)
        except IndexError:
            self.automateNonInitialiserErreur()

    def initialiserEntreeFichier(self, master):
        """
        Fonction qui initialise les entrées lorsqu'on propose d'entrer le nom de fichier.
        paramètres      master (la fenetre des inputs)
        """

        Label(master, text="Nom du fichier   ").grid(row=0)

        nomFichier = Entry(master)
        nomFichier.insert(10, "inventaire.txt")
        nomFichier.grid(row=0, column=1)

        def creer():
            """
            Fonction qui construit l'automate avec le fichier donner en entree''
            """
            if os.path.exists("../data/"+nomFichier.get()):
                self.automate = Automate(nomFichier.get())
                self.canvasPrincipale.itemconfigure("programmeInitialise", state='normal')
                self.canvasPrincipale.itemconfigure("texteACacher", state='hidden')
                self.canvasPrincipale.itemconfigure("imageACacher", state='hidden')
                self.mettreAJourInventaire()
            else:
                messagebox.showerror("Erreur", "Fichier introuvable. Verifiez qu'il se\n"
                                    "situe dans le dossier Data du projet.")
            master.quit()

        Button(master, text='Quitter', command=master.quit).grid(row=1,
                                                                 column=0, sticky=W, pady=4)

        Button(master, text='OK', command=creer).grid(row=1,
                                                              column=1, sticky=E, pady=4)

    def automateNonInitialiserErreur(self):
        """
        Fonction qui génére une erreur quand l'automate n'est
        pas initialisé
        """

        if (self.automate == None):
            messagebox.showerror("Erreur",
                                 'Programme non initialisé!')





