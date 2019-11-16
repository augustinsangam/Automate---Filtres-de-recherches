
from    Chemin                                      import Chemin
from    Commande                                    import Commande
from    Entrepot                                    import Entrepot
from    tkinter                                     import *
from    tkinter                                     import messagebox
from    Interface.PasDeRobotsPossibleError          import PasDeRobotsPossiblesError
from    Interface.CommandeImpossibleError           import CommandeImpossibleError



class Interface(Frame) :
    """
    Classe Interface

    Classe utilisé pour l'affichage de l'interface. On utilise la bibliotèque tkinter
    qui est destiné à créer des interfaces graphiques.
    """

    def __init__(self):
        """
        Constructueur
        param       commande :       La commande de l'utilisateur. Un objet de type commande
        """

        self.commande           =   Commande()
        self.fenetrePrincipale  =   Tk()
        self.canvas             =   None        #le widget principale.
        self.grapheCree         =   False
        self.initialiserGUI()                   #Place les bouttons sur la page d'acceuil


    def initialiserGUI(self, **kwargs):
        """ 
        Fonction qui initialise l'affichage de l'acceuil (au niveau des titres et des dimensions)

        paramètres      liste de widget fournis par la librairie
        """

        Frame.__init__(self, self.fenetrePrincipale, **kwargs)
        self.pack(fill=BOTH)
        self.master.title('Livraison')
        self.canvas = Canvas(self.fenetrePrincipale, width=1200, height=650, background='white')
        self.canvas.create_text(610, 30, text="Bienvenue dans notre système de livraison", font="Arial 20 bold",
                           fill="black")
        self.canvas.create_text(210, 100, text="Veuillez choisir une des options suivantes:", font="Arial 14 bold",
                           fill="black")
        self.canvas.create_text(580, 640, text="@Verbaere Nicolas, Sangam Augustin, Abdelrahman Bassiouni", font="Arial 10 bold",
                                fill="black")

        self.insererBouttons()


    def insererBouttons(self):
        """ 
        Fonction qui insere tous les bouttons de l'interface, et les relient à leurs méthodes
        """

        listeBouttons = []
        listeBouttons.append(
            Button(self.fenetrePrincipale, text="Créer le graphe", command=self.creerGraphe, anchor=W, cursor="hand2"))

        listeBouttons.append(
            Button(self.fenetrePrincipale, text="Afficher le graphe", command=self.afficherGraphe, anchor=W,
                   cursor="hand2"))
        listeBouttons.append(
            Button(self.fenetrePrincipale, text="Prendre la commande", command=self.recupererCommande, anchor=W,
                   cursor="hand2"))

        listeBouttons.append(
            Button(self.fenetrePrincipale, text="Afficher la commande", command=self.afficherCommande, anchor=W,
                   cursor="hand2"))

        listeBouttons.append(
            Button(self.fenetrePrincipale, text="Trouver le plus cours chemin", command=self.cheminLePlusCours,
                   anchor=W,
                   cursor="hand2"))

        listeBouttons.append(
            Button(self.fenetrePrincipale, text="Quitter", command=self.fenetrePrincipale.quit, anchor=W))

        [boutton.configure(width=40, height=2, activebackground="#33B5E5", cursor="hand2", foreground="red") for boutton
         in listeBouttons]

        height = 130
        for element in listeBouttons:
            self.canvas.create_window(20, height, anchor=NW, window=element)
            height += 50
        self.canvas.pack()




    def afficherCommande(self):
        """ 
        Fonction qui affiche la commande de l'utilisateur
        """
        if self.commande.estVide() :
            messagebox.showerror("Erreur", "Aucune commande n'a encore été passée")
        else :
            texte = Text(self.fenetrePrincipale, width=400, height=300, borderwidth=0, font="Arial 13 ", foreground="blue")
            message="""Vous avez commander:\n  -{:>2} colis de type A\n  -{:>2} colis de type B\n  -{:>2} colis de type C
            """.format(self.commande.nA,self.commande.nB,self.commande.nC)
            texte.insert(END, message)
            texte.config(state=DISABLED)
            self.canvas.create_window(350, 150, anchor=NW, height=300, window=texte, tag="affichageCommande")
            self.activerWidjet("affichageCommande")


    def creerGraphe(self) :
        try:
            entrepot = Entrepot()
            if len(entrepot.noeuds) is not 0 :
                self.grapheCree = True
        except FileNotFoundError:
            self.grapheCree = False
        
        if  not self.grapheCree :   
            messagebox.showerror("Erreur", "Le fichier entrepot.txt ne peut pas être lu car il n'a pas été trouvé\n"+
            "Vous pouvez mettre le chemin complet vers le fichier dans le fichier src/entrepot.py")
            return
        else : 
            self.messageCreationGraphe()
            

    def messageCreationGraphe(self):
        """ 
        Fonction qui initialise la classe Entrepot, donc on va construire l'entrepot à partir du fichier texte
        """
        texte = Text(self.fenetrePrincipale, width=400, height=200, borderwidth=0, font="Arial 13 ", foreground="blue")
        texte.insert(END,"Le graphe à bien été créé")
        texte.config(state=DISABLED)
        self.canvas.create_window(350, 150, anchor=NW, window=texte, height=200, tag="creationGraphe")
        self.activerWidjet("creationGraphe")


    def afficherGraphe(self):
        """ 
        Fonction qui affiche fait appel a la fonction d'affichage du reseau de la classe Entrepot
        """
        if not self.grapheCree :
            messagebox.showerror("Erreur", "Il faut d'abord créer un graphe avant de l'afficher")
        else :
            texte = Text(self.fenetrePrincipale,width=400,height=420,  borderwidth=0,font="Arial 13 ", foreground="blue")
            try:
                if Entrepot.instance is None :
                    raise AttributeError()
                for ligne in Entrepot().afficher():
                    texte.insert(END, ligne+ '\n')
            except AttributeError:
                messagebox.showerror("Erreur", "Il faut d'abord créer un graphe avant de l'afficher")
            texte.config(state=DISABLED)
            self.canvas.create_window(350, 150, height=420,  anchor=NW, window=texte, tag="graphe")
            self.activerWidjet("graphe")





    def activerWidjet(self, tag):
        """ 
        Fonction pour afficher les textes approprié en fonction de la situation

        paramètres      le tag du texte à appelé
        """
        self.canvas.itemconfigure("graphe", state='hidden')
        self.canvas.itemconfigure("creationGraphe", state='hidden')
        self.canvas.itemconfigure("affichageCommande", state='hidden')
        self.canvas.itemconfigure("affichageChemin", state='hidden')
        self.canvas.itemconfigure("bouttonLivrerChemin", state='hidden')
        if tag=="affichageChemin" :
            self.canvas.itemconfigure("affichageChemin", state='normal')
            self.canvas.itemconfigure("bouttonLivrerChemin", state='normal')
        else:    
            self.canvas.itemconfigure(tag, state='normal')




    def recupererCommande(self):
        
        """ 
        Fonction déclanchée pour recupérer la commande de l'utilisateur.
        Elle gère la fenetre des inputs.
        """
        if Entrepot.instance is None :
            messagebox.showerror("Erreur", "Il faut d'abord créer un graphe avant de passer une commande")
        else :
            master = Tk()
            master.geometry("350x100+300+300")
            master.title('Commande')
            self.initialiserEntree(master)

            master.mainloop()
            master.destroy()





    def initialiserEntree(self, master):
        """ 
        Fonction qui initialise les entrées lorsqu'on propose d'entrer la commande.
        paramètres      master (la fenetre des inputs)
        """

        Label(master, text="objet de type A  ").grid(row=0)
        Label(master, text="objet de type B  ").grid(row=1)
        Label(master, text="objet de type C  ").grid(row=2)

        nA = Entry(master)
        nB = Entry(master)
        nC = Entry(master)
        nA.insert(10, 0)
        nB.insert(10, 0)
        nC.insert(10, 0)

        nA.grid(row=0, column=1)
        nB.grid(row=1, column=1)
        nC.grid(row=2, column=1)

        
        def creerCommande():
            """ 
            Fonction qui construit la commande à partir des informations entrées par l'utilisateur
            """

            noeudsA, noeudsB, noeudsC = int(nA.get()), int(nB.get()), int(nC.get())
            if (noeudsA < 0 or noeudsB < 0 or noeudsC < 0):
                messagebox.showerror("Erreur", "Il faut fournir des nombres positifs")
            else:
                self.commande.__dict__ = Commande(noeudsA, noeudsB, noeudsC).__dict__
            master.quit()

        
        
        Button(master, text='Quitter', command=master.quit).grid(row=3,
                                                                 column=0, sticky=W, pady=4)

        Button(master, text='OK', command=creerCommande).grid(row=3,
                                                              column=1, sticky=W, pady=4)




    def cheminLePlusCours(self):
        """ 
        Fonction qui fait l'affichage du plus cours chemin. Elle appelle les
        algorithmes de la classe Chemin, qui s'occupe de faire les calculs
        """

        if self.commande.estVide() :
            messagebox.showerror("Erreur",
                                 "Vous devez d'abord faire une commande avant de trouver le meilleur chemin")
        else:

            try :
                resultat = Chemin.cheminLePlusRapide(self.commande.nA,self.commande.nB,self.commande.nC)
                
            except CommandeImpossibleError:
                messagebox.showerror("Erreur",
                                     "Notre entrepot n'a pas en stock tout les objets que vous désirez. Veuillez sélectioner moins de colis")
                return 
            except PasDeRobotsPossiblesError:
                messagebox.showerror("Erreur",
                                     "Nos robots n'ont pas la capacité nécessaire pour satisfaire à la masse de votre commande. Veuillez sélectioner moins de colis") 
                return
            
            
                    
            texte = Text(self.fenetrePrincipale, width=400, height=400,  borderwidth=0, font="Arial 12 bold ", foreground="black")

            nA, nB, nC = self.commande.nA, self.commande.nB, self.commande.nC
            texte.insert(END, "Commande : {} objet(s) de type A, {} objet(s) de type B et {} objet(s) de type C\n".format(nA, nB, nC))
            texte.insert(END, "Robot utilisé :     "+str(resultat["nom"])+ '\n')
            texte.insert(END, "Meilleur temps :  "+ str(resultat["temps"])+ " secondes" '\n\n')
            texte.insert(END, "Parcours (du haut vers le bas): \n")

            self.commande = Commande()
            
            for ceuillette in resultat["parcours"].ceuilletes:
                detailCeuillette=ceuillette.afficherLeNombreDObjetCeuillis()
                if detailCeuillette != "":
                    detailCeuillette = ' ('+detailCeuillette+') '

                texte.insert(END, "Noeud "+ str(ceuillette.noeud.id)+ detailCeuillette + '\n')
            
            texte.config(state=DISABLED)
            if len(resultat["parcours"].ceuilletes)>13:
                texte.configure(font=("Arial", "9", "bold"))
            
            if len(resultat["parcours"].ceuilletes)>17:
                texte.configure(font=("Arial", "7", "bold"))

            self.canvas.create_window(350, 150, anchor=NW, height=400, window=texte, tag="affichageChemin")
            self.activerWidjet("affichageChemin")

            def livrerClient() :
                if resultat is not None :
                    Entrepot().enleverRecolte(resultat['parcours'])


            bouttonLiverCommande = Button(self.fenetrePrincipale, text="Livrer le client (reduire le stock)", command=livrerClient, anchor=W)

            bouttonLiverCommande.configure(width=40, height=2, activebackground="#33B5E5", cursor="hand2", foreground="red")

            self.canvas.create_window(700, 500, anchor=NW, window=bouttonLiverCommande, tag= "bouttonLivrerChemin")
            
            self.canvas.pack()

            



