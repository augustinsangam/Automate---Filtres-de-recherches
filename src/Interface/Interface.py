

from tkinter import ttk
from    tkinter                                     import *
from    tkinter                                     import messagebox




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
        self.canvasPrincipale             =   None        #le widget principale.
        self.canvasCommande     =   None
        self.initialiserGUI()                   #Place les bouttons sur la page d'acceuil


    def initialiserGUI(self, **kwargs):
        """ 
        Fonction qui initialise l'affichage de l'acceuil (au niveau des titres et des dimensions)

        paramètres      liste de widget fournis par la librairie
        """

        Frame.__init__(self, self.fenetrePrincipale, **kwargs)
        self.pack(fill=BOTH)
        self.master.title('Livraison')

        self.canvasPrincipale = Canvas(self.fenetrePrincipale, width=1400, height=650, background='white')
        self.canvasCommande = Canvas(self.fenetrePrincipale, width=600, height=450, background='#e6f2ff',borderwidth=10, relief=RAISED)
        self.canvasPanier= Canvas(self.fenetrePrincipale, width=350, height=450, background='#ffe6e6',borderwidth=10, relief=RAISED)


        self.canvasCommande.place(relx=0.43, rely=0.5, anchor=CENTER)
        self.canvasPanier.place(relx=0.83, rely=0.5, anchor=CENTER)


        self.canvasPrincipale.create_text(710, 30, text="Bienvenue dans notre système de livraison", font="Arial 32 bold",
                                          fill="black")

        self.canvasPrincipale.create_text(710, 640, text="@Verbaere Nicolas, Sangam Augustin, Abdelrahman Bassiouni", font="Arial 10 bold",
                                          fill="black")
        self.canvasPrincipale.create_text(110, 142, text="  Initialiser \nProgramme",
                                          font="Arial 20 bold",
                                          fill="black")

        self.insererBouttons()
        self.insererInputsCommande()
        self.insererInputPanier()


    def insererBouttons(self):
        """ 
        Fonction qui insere tous les bouttons de l'interface, et les relient à leurs méthodes
        """
        photo= PhotoImage(file = r"Play-Button.png")
        label = Label(image=photo)
        label.image = photo  # keep a reference!
        bouttonImage= Button(self.fenetrePrincipale,  image= label.image,command=self.creerGraphe, anchor=CENTER, cursor="hand2")
        bouttonImage.configure(width=150, height=150, activebackground="#33B5E5", cursor="hand2")


        self.canvasPrincipale.create_window(30, 265, anchor=W, window=bouttonImage)
        self.canvasPrincipale.pack()


        bouttonAjouterPanier= Button(self.fenetrePrincipale, text="Ajouter au Panier", command=self.creerGraphe, anchor=CENTER, cursor="hand2")
        bouttonAjouterPanier.configure(width=20, height=1, activebackground="#33B5E5", cursor="hand2", font="Arial 15 bold")
        self.canvasCommande.create_window(40, 400, anchor=W, window=bouttonAjouterPanier)


        bouttonCommander= Button(self.fenetrePrincipale, text="Commander", command=self.creerGraphe,
                                      anchor=CENTER, cursor="hand2")
        bouttonCommander.configure(width=20, height=1, activebackground="#33B5E5", cursor="hand2",
                                       font="Arial 15 bold")
        self.canvasCommande.create_window(330, 400, anchor=W, window=bouttonCommander)


        bouttonRetirerPanier = Button(self.fenetrePrincipale, text="Retirer du Panier", command=self.creerGraphe,
                                 anchor=CENTER, cursor="hand2")
        bouttonRetirerPanier.configure(width=20, height=1, activebackground="#33B5E5", cursor="hand2", font="Arial 15 bold")
        self.canvasPanier.create_window(180, 315, anchor=CENTER, window=bouttonRetirerPanier)



        bouttonViderPanier = Button(self.fenetrePrincipale, text="Vider le Panier", command=self.creerGraphe,
                                 anchor=CENTER, cursor="hand2")
        bouttonViderPanier.configure(width=20, height=1, activebackground="#33B5E5", cursor="hand2", font="Arial 15 bold")
        self.canvasPanier.create_window(180, 385, anchor=CENTER, window=bouttonViderPanier)


    def insererInputsCommande(self):

        self.canvasCommande.create_text(280, 30, text="     Inventaire", font="Arial 24 bold",
                                        fill="black")
        self.canvasCommande.create_text(63, 73, text="  Chosir le type", font="Arial 13 bold",
                                        fill="black")
        self.canvasCommande.create_text(263, 73, text="  Ecrire le code", font="Arial 13 bold",
                                        fill="black")
        self.canvasCommande.create_text(463, 73, text="  Ecrire le nom", font="Arial 13 bold",
                                        fill="black")


        comboExample = ttk.Combobox(self.fenetrePrincipale,
                                    values=["",
                                        "A",
                                        "B",
                                        "C"], width=12)
        comboExample.place(relx=0.252, rely=0.29, anchor=CENTER)
        comboExample.current(0)


        inputCode=StringVar(self.fenetrePrincipale, value='')
        inputNom=StringVar(self.fenetrePrincipale, value='')
        inputCodeWidget = Entry(self.fenetrePrincipale,textvariable=inputCode, borderwidth=2, width=14)
        inputNomWidget = Entry(self.fenetrePrincipale, borderwidth=2, textvariable=inputNom)
        inputCodeWidget.pack()
        inputNomWidget.pack()
        self.canvasCommande.create_window(215, 96, anchor=W, window=inputCodeWidget)
        self.canvasCommande.create_window(415, 96, anchor=W, window=inputNomWidget)

        frame = Frame(self.fenetrePrincipale)
        frame.place(relx=0.36, rely=0.53, anchor=CENTER)
        listeInventaire = Listbox(frame, width=37, font="Helvetica 12 ")
        listeInventaire.pack(side="left", fill="y")
        scrollbar = Scrollbar(frame, orient="vertical")
        scrollbar.config(command=listeInventaire.yview)
        scrollbar.pack(side="right", fill="y")
        listeInventaire.config(yscrollcommand=scrollbar.set)
        for item in ["on3333333333333333333333e", "two333333333333333", "three333333333333333333", "fou333333333333333r"]:
            listeInventaire.insert(END, item)

        self.canvasCommande.create_text(140, 140, text=" 56 elements correspondant", font="Arial 13 bold",
                                        fill="black")


    def insererInputPanier(self):

        self.canvasPanier.create_text(190, 30, text="Panier", font="Arial 24 bold",
                                      fill="black")
        frame = Frame(self.fenetrePrincipale)
        frame.place(relx=0.83, rely=0.4, anchor=CENTER)

        listePanier = Listbox(frame, width=30, height=10, font=("Helvetica", 12))
        listePanier.pack(side="left", fill="y")

        scrollbar = Scrollbar(frame, orient="vertical")
        scrollbar.config(command=listePanier.yview)
        scrollbar.pack(side="right", fill="y")

        listePanier.config(yscrollcommand=scrollbar.set)

        for x in range(100):
            listePanier.insert(END, str(x))



    def creerGraphe(self) :
        print("lol")


