####################################################################################
#   Fichier     :   Automate.py
#   Auteur      :   EyaTom Augustin SANGAM & AbdelRahman Mohammed Bassiouni 
#                       & Nicolas Verbaere
#   Date        :   17 Novembre 2019
#   Projet      :   Automate : Filtres de recherches
####################################################################################

from collections    import defaultdict

from Etat           import Etat

class Automate(object):
    """

    Classe Automate

    Classe qui modélise l'automate 
    L'automate est unique

    """

    instance = None       # Attribut statique de classe

    def __new__(cls,nomFichier):
        """
        Méthode de construction standard en Python
        Elle suit l'implémentation d'une classe Singleton comme défini ici :
        https://fr.wikipedia.org/wiki/Singleton_(patron_de_conception)#Python
        """

        if cls.instance is None:
            cls.instance            = object.__new__(cls)
            cls.instance.memoire    = defaultdict(set)     # La mémoire associée à l'automate. Elle contient tous les états possible
                                                            # Il est censé être une map< Etat, list < str > >
            cls.instance.creerAutomate("../data/"+nomFichier)
            #cls.instance.creerAutomate("../data/gros_inventaire.txt") # Fichier pour tester le programme avec un gros inventaire
                                                                      # pour s'assurer des performances. L'initialisation demande au maximum 10 secondes

        return cls.instance


    def creerAutomate(self, nomFichier) :
        """
        Méthode creerAutomate(nomFichier)
        Permet de lire le fichier et de créer l'automate

        param nomFichier    : Le chemin vers le fichier contenant les données
        """
        # On ouvre le fichier et on lit tous les lignes du fichier
        with open (nomFichier, 'r') as fichier :
            ligne = fichier.readline().strip()
            while ligne :
                etat = Etat(*(ligne.split(' ')))
                self.ajouterEtat(etat)
                ligne = fichier.readline().strip()

    

    def __getitem__(self, etat):
        """
        Méthode spéciale __getitem__
        Surchage de l'opérateur []

        param       etat :   L'état pour lequel on cherche des informations

        Retourne une liste itérable d'élement matchants avec l'état spécifié
        """
        if type(etat) == Etat :
            return self.memoire[Etat.freeze(etat)]
        return self.memoire[etat]


    def ajouterEtat(self,etat):
        """
        Méthode ajouterEtat(etat) :

        Permet d'ajouter un état à l'automate

        param       etat    :   L'état à ajouter

        """

        for etatPrecedent in etat.genererEtatsValidesPrecedents():
            self.memoire[Etat.freeze(etatPrecedent)].add(etat)

    def enleverEtat(self, etat) :
        """
        Méthode enleverEtat(etat) :

        Permet d'enlever un état de l'automate

        param       etat    :   L'état à enlever

        """
        for etatPrecedent in etat.genererEtatsValidesPrecedents() :
            self.memoire[Etat.freeze(etatPrecedent)].remove(etat)



    def obtenirChoixPossibles(self, etat) :
        """
        Méthode obtenirChoixPossibles(etat)
        Donne le nombre d'objets et dix objets correspondant à la recherche

        param       etat    :   L'état recherché

        return      Un tuple conteant, nombre d'objets et dix objets correspondant à la recherche
        """
        tousLesChoix = self[etat]
        #return (len(tousLesChoix), self.genererNElement(tousLesChoix, 100))
        return (len(tousLesChoix), list(tousLesChoix)[0:100])


    def __iadd__(self, etat):
        """
        Méthode spéciale __iadd__
        Surchage de l'opérateur +=

        Permet d'ajouter un état à l'automate

        param       etat    :   L'état à ajouter

        """
        self.ajouterEtat(etat)
        return self

    def __isub__(self, etat) :
        """
        Méthode spéciale __isub__
        Surchage de l'opérateur -=

        Permet d'enlever un état de l'automate

        param       etat    :   L'état à enlever

        """

        self.enleverEtat(etat)
        return self

