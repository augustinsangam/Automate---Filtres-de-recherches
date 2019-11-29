####################################################################################
#   Fichier     :   Panier.py
#   Auteur      :   EyaTom Augustin SANGAM & AbdelRahman Mohammed Bassiouni 
#                       & Nicolas Verbaere
#   Date        :   28 Novembre 2019
#   Projet      :   Automate : Filtres de recherches
####################################################################################

from Interface.CommandeImpossibleError import CommandeImpossibleError

class Panier(set) :
    """
    Classe Panier

    Classe qui représente un panier
    
    Un panier est une liste d'objets à laquelle est asscocié un poids
    """

    poidsMaximal = 25       # Attribut statique contenant le poids

    def __init__(self) :
        """
        Constructueur
        """
        super().__init__()
        self.poids  = 0



    def ajouter(self, objet) :
        """
        Méthode add(objet)

        Ajoute permet d'ajouter l'objet au panier

        param       objet   :   L'objet à ajouter
        """

        nouveauPoids = self.poids + Panier.poids(objet.obtenirChaine()[-1])  # Le dernier caractère représente le type

        if nouveauPoids > Panier.poidsMaximal :
            raise CommandeImpossibleError('Panier trop lourd !')
        else :
            super().add(objet)
            self.poids = nouveauPoids 




    def __iadd__(self, objet) :
        """
        Méthode spéciale __iadd__(objet)
        Surcharge de l'opérateur +=

        Ajoute permet d'ajouter l'objet au panier

        param       objet   :   L'objet à ajouter
        """

        self.ajouter(objet)
        return self
    


    def retirer(self, objet) :
        """
        Méthode retirer(objet)

        Retire l'objet du panier

        param       objet   :   L'objet à retirer
        """

        super().remove(objet)
        self.poids -= Panier.poids(objet.obtenirChaine()[-1]) # Le dernier caractère représente le type



    def __isub__(self, objet) :
        """
        Méthode spéciale __isub__(objet)
        Surcharge de l'opérateur -=

        Retire l'objet au panier

        param       objet   :   L'objet à retirer
        """

        self.retirer(objet)
        return self




    def vider(self) :
        """
        Méthode vider
        Permet de vider tous le panier
        """
        
        super().clear()
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



    


