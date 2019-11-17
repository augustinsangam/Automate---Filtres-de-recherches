####################################################################################
#   Fichier     :   Etat.py
#   Auteur      :   EyaTom Augustin SANGAM & AbdelRahman Mohammed Bassiouni 
#                       & Nicolas Verbaere
#   Date        :   17 Novembre 2019
#   Projet      :   Itinéraire rapide - Drone collecteur
####################################################################################

class Etat(object):
    """
    Classe Etat

    Classe qui représente une Etat d'une recherche.
    Elle est définie par l'entrée au niveau du type, du code et du nom
    
    """

    def __init__(self, nom, code, type) :
        """
        Constructueur
        param    nom    :    Le nom
        param    code   :    Le code
        param    type   :    Le type

        """
        self.nom    = nom
        self.code   = code
        self.type   = type

    def obtenirChaine(self) :
        """
        Méthode obtenirChaine
       
        Retourne la chaine de caractère décrivant l'objet au complet
        """
        return ' '.join([self.nom, self.code, self.type])

    def genererEtatsValidesPrecedents(self) :
        """
        Méthode genererEtatsValidesPrecedents
        
        Un générateur qui renvoit tous les états valides précédent l'état courant
        """
        for i in range(len(self.nom) + 1 ) :
            for j in range(len(self.code) + 1 ) :
                for k in range(len(self.type) + 1 ) :
                    yield Etat(self.nom[0:i], self.code[0:j], self.type[0:k])


    ##############################################################################
    # Petite paranthèse : Le freeze                                              #
    # Cette classe sera utilisée par la suite comme étant une clé dans une map   #
    # (dictionnaire dans le jargon python).                                      #
    # On aime souvent avoir des clés immuables pour les tables de hashage pour   #
    # s'assurer déja de bien faire le hashage sur des valeurs et non des         #
    # adreses de objets                                                          #
    # La fonction freeze nous permet de transformer cet objet en un tuple        #
    # (les tuples étant immuables en python)                                     #
    ##############################################################################

    @staticmethod
    def freeze(etat) :
        """
        Fonction freee

        param       etat     :  Un objet de type Etat

        return      Un représentation immuable de l'objet sous forme de tuple
        """
        return (etat.nom, etat.code, etat.type)

    @staticmethod
    def unfreeze(etat) :
        """
        Fonction unfreee

        param       etat    :  Un Etat sous sa forme immuable (tuple)

        return      Un représentation normale de l'objet
        """
        return Etat(etat[0], etat[1], etat[2])


