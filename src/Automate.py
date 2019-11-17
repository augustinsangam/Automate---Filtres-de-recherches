####################################################################################
#   Fichier     :   Automate.py
#   Auteur      :   EyaTom Augustin SANGAM & AbdelRahman Mohammed Bassiouni 
#                       & Nicolas Verbaere
#   Date        :   17 Novembre 2019
#   Projet      :   Itinéraire rapide - Drone collecteur
####################################################################################

from collections import defaultdict

from Etat import Etat

class Automate(object):
    """

    Classe Automate

    Classe qui modélise l'automate 
    L'automate est unique

    """

    instance = None       # Attribut statique de classe

    def __new__(cls): 
        """
        Méthode de construction standard en Python
        Elle suit l'implémentation d'une classe Singleton comme défini ici :
        https://fr.wikipedia.org/wiki/Singleton_(patron_de_conception)#Python
        """

        if cls.instance is None:
            cls.instance            = object.__new__(cls)
            cls.instance.memoire    = defaultdict(set)     # La mémoire associée à l'automate. Elle contient tous les états possible
                                                            # Il est censé être une map< Etat, list < str > >
            cls.instance.creerAutomate("../data/inventaire.txt")

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
                for etatPrecedent in etat.genererEtatsValidesPrecedents() :
                    self.memoire[Etat.freeze(etatPrecedent)].add(ligne)
                ligne = fichier.readline().strip()

    

    def __getitem__(self, key):
        """
        Méthode spéciale __getitem__
        Surchage de l'opérateur []

        param       key :   L'état pour lequel on cherche des informations

        Retourne une liste itérable d'élement matchants avec l'état spécifié
        """
        if type(key) == Etat :
            return self.memoire[Etat.freeze(key)]
        return self.memoire[key]




    def enleverEtat(self, etat) :
        """
        Méthode enleverEtat(etat) :

        Permet d'enlever un état de l'automate

        param       etat    :   L'état à enlever

        """
        for etatPrecedent in etat.genererEtatsValidesPrecedents() :
            self.memoire[Etat.freeze(etatPrecedent)].remove(etat.obtenirChaine())

    

    def __isub__(self, etat) :
        """
        Méthode spéciale __isub__
        Surchage de l'opérateur -=

        Permet d'enlever un état de l'automate

        param       etat    :   L'état à enlever

        """

        self.enleverEtat(etat)
        return self
