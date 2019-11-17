####################################################################################
#   Fichier     :   Panier.py
#   Auteur      :   EyaTom Augustin SANGAM & AbdelRahman Mohammed Bassiouni 
#                       & Nicolas Verbaere
#   Date        :   17 Novembre 2019
#   Projet      :   Itinéraire rapide - Drone collecteur
####################################################################################

class Panier(object) :
    """
    Classe Panier

    Classe qui représente un panier
    
    Un panier est une liste d'objets auqeul est asscocié un poids
    """


    def __init__(self) :
        """
        Constructueur
        """
        self.objets = set()
        self.poids  = 0



    def ajouter(self, objet) :
        """
        Méthode add(objet)

        Ajoute permet d'ajouter l'objet au panier

        param       objet   :   L'objet à ajouter
        """

        self.objets.add(objet)
        self.poids += Panier.poids(objet[-1]) # Le dernier caractère représente le type



    def retirer(self, objet) :
        """
        Méthode retirer(objet)

        Retire l'objet du panier

        param       objet   :   L'objet à retirer
        """

        self.objets.remove(objet)
        self.poids -= Panier.poids(objet[-1]) # Le dernier caractère représente le type



    def vider(self) :
        """
        Méthode vider
        Permet de vider tous le panier
        """
        
        self.objets = set()
        self.poids  = 0



    def poids(type) :
        """
        Fonction poids(type)

        Retourne le poids de l'objet en fonction dy type
        Génère une exception de type AttributeError si le type n'a pas pu
        être reconnu

        param       type    :   Le type d'objet. ('A', 'B' ou 'C')

        return      Le poids associé au ty[w
        """
        if type == 'A' :
            return 1
        elif type == 'B' :
            return 3
        elif type == 'C' :
            return 6
        else :
            raise AttributeError



    


